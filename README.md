# apinoa

The official Python SDK for [apinoa](https://apinoa.com): product data from Amazon, Walmart, Shopify,
TikTok Shop and AliExpress; posts, profiles and comments from TikTok, YouTube, Instagram, Threads, X, Reddit
and LinkedIn; search results from Google, Bing, Naver and 13 more search engines; AI answers from ChatGPT,
Gemini, Google AI Overviews, Google AI Mode and Naver; and image translation, through one API.

```sh
pip install apinoa
```

Requires Python 3.9 or later.

## Usage

Create a key under **Dashboard > API keys** at [apinoa.com](https://apinoa.com), then:

```python
from apinoa import Apinoa

client = Apinoa()  # reads APINOA_API_KEY; or Apinoa(api_key="...")

res = client.amazon.search(query="wool socks", price_max=30)
for item in res.data.items:
    print(item.title, item.price.amount if item.price else None)
```

Keep the key on your server: it spends your balance.

Every call is `client.<platform>.<operation>(...)`, spelled the way the URL is, in snake_case:
`/v1/amazon/image-search` is `client.amazon.image_search(...)`, and the parameter `priceMax` is
`price_max`. Every answer is `{ success, data, request_id }`; fields beyond the documented ones are kept
on the object.

### Marketplaces

Every marketplace answers in one commerce schema: a `Product` from Amazon reads like one from Shopify.

```python
product = client.walmart.product(id="18256507800")
reviews = client.shopify.reviews(id="allbirds.com/products/mens-tree-runners")
tree = client.amazon.categories()
```

### Social platforms

Every platform answers in one social schema (`Account`, `Post`, `Comment`, `Group`), with what only one
platform has under `ext`.

```python
creator = client.tiktok.profile(username="khaby.lame")
page = client.reddit.posts(community="python")
next_page = client.reddit.posts(cursor=page.data.cursor)  # the next page: the cursor alone
```

### Search engines

Every search engine answers in one results-page schema: Google, Bing, Naver, Baidu, Yandex, Yahoo and the
rest return the same `items`.

```python
res = client.google.search(q="trail running shoes", country="US")
for item in res.data.items:
    if item.type == "organic":
        print(item.position, item.title, item.url)
naver = client.naver.search(q="러닝화 추천")
```

### AI answers

What ChatGPT, Gemini, Google AI Overviews, Google AI Mode and Naver answer to a prompt, with its citations,
sources and the brands it names, in one `Answer` type.

```python
ans = client.chatgpt.answer(prompt="Best running shoes for beginners?", country="US")
print(ans.data.text)
cited = [s.url for s in ans.data.sources if s.cited]
aio = client.google_aio.answer(prompt="best running shoes for beginners")
```

### Image translation

```python
with open("product.jpg", "rb") as f:
    image = f.read()

translated = b"".join(
    client.image_translate.translate(source_language="zh-CN", target_language="ko", request=image)
)
with open("translated.jpg", "wb") as f:
    f.write(translated)
```

### OCR

```python
with open("product.jpg", "rb") as f:
    result = client.ocr.read(request=f.read())

for region in result.data.regions:
    print(region.text, region.confidence)
```

`language` (`zh-CN`, `zh-TW`, `ja`, `en`) keeps only the text in that language; the default, `auto`, returns all of it.

## Async

`AsyncApinoa` has the same methods, awaitable:

```python
import asyncio
from apinoa import AsyncApinoa

async def main() -> None:
    client = AsyncApinoa()
    res = await client.youtube.profile(username="@mkbhd")
    print(res.data.display_name)

asyncio.run(main())
```

## Errors

A failed call raises a subclass of `apinoa.core.ApiError` named after its status (`BadRequestError`,
`PaymentRequiredError`, `NotFoundError`, `TooManyRequestsError`, …). `err.body.error.code` is the stable
code to branch on; every code is listed at [apinoa.com/docs/errors](https://apinoa.com/docs/errors). A
failed call is not billed.

```python
from apinoa import NotFoundError, PaymentRequiredError

try:
    client.amazon.product(id="B000000000")
except NotFoundError:
    print("no such product")
except PaymentRequiredError:
    print("top up your balance")
```

## Retries and timeouts

`429`, `408` and `5xx` answers are retried twice with exponential backoff, honouring `Retry-After`. The
default timeout is 300 seconds, because image translation under load can take minutes. Both can be set
per client or per call:

```python
client = Apinoa(max_retries=4, timeout=60)
client.tiktok.posts(username="nasa", request_options={"max_retries": 0, "timeout_in_seconds": 10})
```

## Examples

[`examples/`](./examples) holds four small programs to copy and adapt: a price tracker, a rank tracker,
social listening and an AI-answer monitor. Each is one file that runs with `python`.

## Reference

Every method and parameter: [reference.md](./reference.md). The API itself:
[apinoa.com/docs](https://apinoa.com/docs). The OpenAPI document this SDK is generated from:
[apinoa.com/openapi.json](https://apinoa.com/openapi.json).

## License

MIT
