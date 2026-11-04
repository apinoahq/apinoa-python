"""AI-answer monitor: ask AI answer engines a buyer's question and record whether your brand is named in
the answer, what the engine itself marked (brands, products, places), and which sources it cites.
Appends to answers.csv.

    python ai_answer_monitor.py "best wool socks for hiking" "Darn Tough"
    python ai_answer_monitor.py "best wool socks for hiking" "Darn Tough" --engines chatgpt,gemini,google-aio

An answer can take a minute or two. Answers vary from one ask to the next, so run the same prompt on a
schedule and read the trend, not one result.
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
from urllib.parse import urlparse

from apinoa import Apinoa

ENGINES = {"chatgpt": "chatgpt", "gemini": "gemini", "google-aio": "google_aio", "google-ai-mode": "google_ai_mode"}
FILE = "answers.csv"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("prompt")
    p.add_argument("brand")
    p.add_argument("--engines", default="chatgpt")
    a = p.parse_args()
    client = Apinoa(timeout=300)  # reads APINOA_API_KEY

    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        out = csv.writer(f)
        if new_file:
            out.writerow(["asked_at", "engine", "prompt", "brand", "named", "marked_by_engine", "cited_sources"])
        for engine in a.engines.split(","):
            if engine not in ENGINES:
                print(f'unknown engine "{engine}"', file=sys.stderr)
                continue
            try:
                answer = getattr(client, ENGINES[engine]).answer(prompt=a.prompt).data
            except Exception as err:  # failed calls are not billed
                print(f"{engine}: {err}", file=sys.stderr)
                continue
            if answer.outcome in ("noAnswer", "refused"):
                print(f"{engine}: {answer.outcome}")
                continue
            # Mentions are only what the engine marked itself, often nothing; "named" searches the answer's text.
            marked = [m.name for m in answer.mentions]
            named = a.brand.lower() in answer.text.lower()
            cited = sorted({urlparse(s.url).hostname or s.url for s in answer.sources if s.cited})
            print(f"{engine}: {a.brand} {'is' if named else 'is not'} named. Marked: {', '.join(marked) or 'nothing'}. Cited: {', '.join(cited) or 'none'}")
            out.writerow([answer.asked_at.isoformat(), engine, a.prompt, a.brand, named, "; ".join(marked), "; ".join(cited)])


if __name__ == "__main__":
    main()
