"""Against the real API, with a real key: APINOA_API_KEY=... pytest tests/live
Three calls, each one unit at most. Skipped without a key."""

import os

import pytest

from apinoa import Apinoa

pytestmark = pytest.mark.skipif(not os.getenv("APINOA_API_KEY"), reason="set APINOA_API_KEY to run the live tests")


def client() -> Apinoa:
    return Apinoa(**({"base_url": os.environ["APINOA_BASE_URL"]} if os.getenv("APINOA_BASE_URL") else {}))


def test_catalog_lists_every_platform() -> None:
    ids = {m.id for m in client().marketplaces.list().data.marketplaces}
    assert {"amazon", "walmart", "reddit", "tiktok"} <= ids


def test_social_profile() -> None:
    res = client().reddit.profile(username="spez")
    assert res.data.platform == "reddit"
    assert res.data.handle.lower() == "spez"


def test_marketplace_search() -> None:
    res = client().walmart.search(query="wool socks")
    assert res.data.items
    assert res.data.items[0].title
