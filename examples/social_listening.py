"""Social listening: new posts that mention a term, on Reddit, Threads or YouTube. Remembers what it has
shown in seen.json, so each run prints only what is new.

    python social_listening.py "your brand"
    python social_listening.py "your brand" --platforms reddit,youtube

Every platform answers in the same social schema, so one loop reads them all.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

from apinoa import Apinoa

FILE = "seen.json"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("term")
    p.add_argument("--platforms", default="reddit")
    a = p.parse_args()
    client = Apinoa()  # reads APINOA_API_KEY

    search = {
        "reddit": lambda q: client.reddit.posts(query=q, sort="new"),
        "threads": lambda q: client.threads.posts(query=q),
        "youtube": lambda q: client.youtube.posts(query=q),
    }
    seen = set(json.load(open(FILE))) if os.path.exists(FILE) else set()
    fresh = 0
    for platform in a.platforms.split(","):
        if platform not in search:
            print(f'unknown platform "{platform}"', file=sys.stderr)
            continue
        try:
            page = search[platform](a.term).data
        except Exception as err:  # failed calls are not billed
            print(f"{platform}: {err}", file=sys.stderr)
            continue
        for post in page.items:
            key = f"{post.platform}:{post.id}"
            if key in seen:
                continue
            seen.add(key)
            fresh += 1
            text = " ".join((post.title or post.text or "").split())[:120]
            print(f"[{post.platform}] {post.author.handle or ''}: {text}\n  {post.url}")
    with open(FILE, "w") as f:
        json.dump(sorted(seen), f)
    print(f"{fresh} new" if fresh else "nothing new")


if __name__ == "__main__":
    main()
