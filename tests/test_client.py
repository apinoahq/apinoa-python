"""The SDK against a fake of the API (httpx.MockTransport): what goes on the wire, and what comes back."""

import json
import typing

import httpx
import pytest

from apinoa import Apinoa, AsyncApinoa
from apinoa import BadGatewayError, BadRequestError, PaymentRequiredError
from apinoa.core.api_error import ApiError

Responder = typing.Callable[[httpx.Request, int], httpx.Response]


class Fake:
    def __init__(self, respond: Responder) -> None:
        self.respond = respond
        self.seen: typing.List[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        request.read()
        self.seen.append(request)
        return self.respond(request, len(self.seen))


def ok(data: typing.Any, **extra: typing.Any) -> httpx.Response:
    return httpx.Response(200, json={"success": True, "data": data, **extra})


def fail(status: int, code: str, headers: typing.Optional[dict] = None) -> httpx.Response:
    return httpx.Response(status, json={"success": False, "error": {"code": code, "message": code.lower()}}, headers=headers)


def client(fake: Fake, **kw: typing.Any) -> Apinoa:
    return Apinoa(api_key="ak_test", base_url="https://api.test", httpx_client=httpx.Client(transport=httpx.MockTransport(fake)), **kw)


def test_get_sends_key_and_query_lists_comma_joined_and_returns_envelope() -> None:
    fake = Fake(lambda r, n: ok({"marketplace": "amazon", "page": {"index": 1}, "items": [{"id": "B0", "title": "Socks", "extra": 1}]}, requestId="r1"))
    res = client(fake).amazon.search(query="wool socks", brands=["Nike", "Adidas"], price_min=5)
    [req] = fake.seen
    assert req.method == "GET"
    assert req.url.path == "/v1/amazon/search"
    assert req.url.params["query"] == "wool socks"
    assert req.url.params["brands"] == "Nike,Adidas"
    assert req.url.params["priceMin"] == "5"
    assert req.headers["x-api-key"] == "ak_test"
    assert res.success is True
    assert res.request_id == "r1"
    item = res.data.items[0]
    assert item.title == "Socks"
    assert item.extra == 1, "fields beyond the declared type are kept"


def test_key_falls_back_to_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APINOA_API_KEY", "ak_from_env")
    fake = Fake(lambda r, n: ok({"platform": "reddit", "handle": "spez", "url": "https://reddit.com/u/spez"}))
    Apinoa(base_url="https://api.test", httpx_client=httpx.Client(transport=httpx.MockTransport(fake))).reddit.profile(username="spez")
    assert fake.seen[0].headers["x-api-key"] == "ak_from_env"


def test_image_search_posts_json_body() -> None:
    fake = Fake(lambda r, n: ok({"marketplace": "amazon", "page": {"index": 1}, "items": []}))
    client(fake).amazon.image_search(image={"contentType": "image/jpeg", "data": "AAAA"})
    [req] = fake.seen
    assert req.method == "POST"
    assert json.loads(req.content) == {"image": {"contentType": "image/jpeg", "data": "AAAA"}}


def test_400_raises_with_code_and_is_not_retried() -> None:
    fake = Fake(lambda r, n: fail(400, "INVALID_PARAMS"))
    with pytest.raises(BadRequestError) as e:
        client(fake).walmart.search(query="x")
    assert e.value.status_code == 400
    assert e.value.body.error.code == "INVALID_PARAMS"
    assert len(fake.seen) == 1


def test_402_raises_and_is_not_retried() -> None:
    fake = Fake(lambda r, n: fail(402, "INSUFFICIENT_BALANCE"))
    with pytest.raises(PaymentRequiredError):
        client(fake).walmart.search(query="socks")
    assert len(fake.seen) == 1


def test_429_is_retried_after_retry_after_then_succeeds() -> None:
    fake = Fake(lambda r, n: fail(429, "CAPACITY_SATURATED", {"retry-after": "0"}) if n == 1 else ok({"marketplace": "walmart", "page": {"index": 1}, "items": []}))
    res = client(fake).walmart.search(query="socks")
    assert len(fake.seen) == 2
    assert res.data.items == []


def test_persistent_502_gives_up_after_max_retries() -> None:
    fake = Fake(lambda r, n: fail(502, "UPSTREAM_TIMEOUT"))
    with pytest.raises(BadGatewayError):
        client(fake, max_retries=1).tiktok.posts(username="x")
    assert len(fake.seen) == 2


def test_errors_share_one_base_class() -> None:
    fake = Fake(lambda r, n: fail(404, "PRODUCT_NOT_FOUND"))
    with pytest.raises(ApiError):
        client(fake).walmart.product(id="0")


def test_image_translation_uploads_raw_bytes_and_returns_the_image() -> None:
    jpeg = bytes([0xFF, 0xD8, 0xFF, 0xE0, 1, 2, 3])
    fake = Fake(lambda r, n: httpx.Response(200, content=bytes([0xFF, 0xD8, 9, 9]), headers={"content-type": "image/jpeg"}))
    out = b"".join(client(fake).image_translate.translate(source_language="zh-CN", target_language="ko", request=jpeg))
    [req] = fake.seen
    assert req.method == "POST"
    assert req.url.path == "/v1/image-translate/translate"
    assert req.url.params["source_language"] == "zh-CN"
    assert req.url.params["target_language"] == "ko"
    assert req.content == jpeg
    assert out == bytes([0xFF, 0xD8, 9, 9])


def test_ocr_uploads_raw_bytes_and_returns_the_regions() -> None:
    png = bytes([0x89, 0x50, 0x4E, 0x47, 1, 2, 3])
    regions = {"regions": [{"index": 0, "text": "限时特价", "confidence": 0.99}], "regions_found": 1, "src_w": 750, "src_h": 750}
    fake = Fake(lambda r, n: ok(regions))
    res = client(fake).ocr.read(request=png)
    [req] = fake.seen
    assert req.method == "POST"
    assert req.url.path == "/v1/ocr"
    assert "language" not in req.url.params
    assert req.content == png
    assert res.data.regions[0].text == "限时特价"

    fake = Fake(lambda r, n: ok(regions))
    client(fake).ocr.read(request=png, language="ja")
    assert fake.seen[0].url.params["language"] == "ja"


def test_catalog_lists_platforms() -> None:
    fake = Fake(lambda r, n: ok({"marketplaces": [{"id": "walmart", "kind": "marketplace", "operations": ["search"]}]}))
    assert client(fake).marketplaces.list().data.marketplaces[0].id == "walmart"


async def test_async_client() -> None:
    fake = Fake(lambda r, n: ok({"platform": "tiktok", "handle": "nasa", "url": "https://tiktok.com/@nasa"}))
    c = AsyncApinoa(api_key="k", base_url="https://api.test", httpx_client=httpx.AsyncClient(transport=httpx.MockTransport(fake)))
    res = await c.tiktok.profile(username="nasa")
    assert res.data.handle == "nasa"


def test_a_social_page_serializes_to_json() -> None:
    post = {"platform": "x", "id": "1", "url": "https://x.com/a/status/1", "text": "hi", "createdAt": "2026-10-20T23:24:11Z",
            "author": {"platform": "x", "handle": "a"}, "metrics": {"likes": 2, "views": 30},
            "media": [{"type": "image", "url": "https://cdn/i.jpg", "variants": [{"url": "https://cdn/i-s.jpg"}]}]}
    fake = Fake(lambda r, n: ok({"platform": "x", "items": [post], "cursor": "c2"}))
    res = client(fake).x.posts(username="a")
    for dumped in (json.loads(res.model_dump_json(by_alias=True)), res.model_dump(mode="json", by_alias=True), res.dict(by_alias=True)):
        item = dumped["data"]["items"][0]
        assert item["metrics"]["views"] == 30
        assert item["media"][0]["variants"][0]["url"] == "https://cdn/i-s.jpg"
    assert json.loads(res.model_dump_json(by_alias=True))["data"]["items"][0]["createdAt"].startswith("2026-10-20T23:24:11")


def test_feedback_send_posts_the_report_and_get_reads_the_reply() -> None:
    fid = "fb_0123456789abcdef0123456789abcdef"

    def respond(r: httpx.Request, n: int) -> httpx.Response:
        if r.method == "POST":
            return httpx.Response(201, json={"success": True, "data": {"id": fid, "status": "received", "createdAt": "2026-11-11T10:00:00Z"}})
        return ok({"id": fid, "type": "error", "status": "resolved", "reply": None, "repliedAt": None, "createdAt": "2026-11-11T10:00:00Z", "updatedAt": "2026-11-11T10:00:00Z"})

    fake = Fake(respond)
    c = client(fake)
    sent = c.feedback.send(type="error", message="search returned no prices", platform="amazon", operation="search", params={"query": "socks"}, request_id="r1")
    post = fake.seen[0]
    assert post.method == "POST"
    assert post.url.path == "/v1/feedback"
    assert post.headers["x-api-key"] == "ak_test"
    assert json.loads(post.content) == {
        "type": "error",
        "message": "search returned no prices",
        "platform": "amazon",
        "operation": "search",
        "params": {"query": "socks"},
        "requestId": "r1",
    }
    assert sent.data.id == fid
    status = c.feedback.get(fid)
    assert fake.seen[1].url.path == f"/v1/feedback/{fid}"
    assert status.data.status == "resolved"
    assert status.data.reply is None
