"""Rank tracker: where does a site rank for a query, on each search engine? Appends to ranks.csv.

    python rank_tracker.py "wool socks" example.com
    python rank_tracker.py "wool socks" example.com --engines google,bing,naver --country US --pages 2

One page is one call. Each engine returns the same results-page schema, so the same code reads them all.
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
from datetime import datetime, timezone
from urllib.parse import urlparse

from apinoa import Apinoa

ENGINES = ("google", "bing", "duckduckgo", "naver")  # Naver searches Korea and takes no country
FILE = "ranks.csv"


def is_ours(url: str, domain: str) -> bool:
    host = urlparse(url).hostname or ""
    if host.startswith("www."):
        host = host[4:]
    return host == domain or host.endswith("." + domain)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("query")
    p.add_argument("domain")
    p.add_argument("--engines", default="google")
    p.add_argument("--country", help="ISO code, upper case, e.g. US")
    p.add_argument("--pages", type=int, default=1)
    a = p.parse_args()
    client = Apinoa()  # reads APINOA_API_KEY

    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        out = csv.writer(f)
        if new_file:
            out.writerow(["checked_at", "engine", "query", "domain", "rank", "url"])
        for engine in a.engines.split(","):
            if engine not in ENGINES:
                print(f'unknown engine "{engine}"', file=sys.stderr)
                continue
            found = None
            cursor = None
            checked = 0
            try:
                for _ in range(a.pages):
                    params = {"q": a.query, "cursor": cursor}
                    if a.country and engine != "naver":
                        params["country"] = a.country.upper()
                    page = getattr(client, engine).search(**params).data
                    # Organic results carry their position among organic results; ads, maps and videos are skipped.
                    organic = [i for i in page.items if i.type == "organic"]
                    checked += len(organic)
                    found = next(((i.position, i.url) for i in organic if is_ours(i.url, a.domain)), None)
                    cursor = page.cursor
                    if found or not cursor:
                        break
            except Exception as err:  # failed calls are not billed
                print(f"{engine}: {err}", file=sys.stderr)
                continue
            print(f"{engine}: #{found[0]} {found[1]}" if found else f"{engine}: not in the first {checked} organic results")
            out.writerow([datetime.now(timezone.utc).isoformat(), engine, a.query, a.domain, found[0] if found else "", found[1] if found else ""])


if __name__ == "__main__":
    main()
