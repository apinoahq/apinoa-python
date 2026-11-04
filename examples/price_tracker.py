"""Price tracker: read each product's price now, keep the history in prices.csv, and say what changed
since the last run.

    python price_tracker.py walmart 18256507800 shopify allbirds.com/products/mens-tree-runners

Arguments come in pairs: a marketplace (amazon, walmart, shopify, aliexpress, tiktokshop) and a product
id or URL. Run it on a schedule (cron, a CI job) to build the history.
"""
from __future__ import annotations

import csv
import os
import sys
from datetime import datetime, timezone

from apinoa import Apinoa

MARKETPLACES = ("amazon", "walmart", "shopify", "aliexpress", "tiktokshop")
FILE = "prices.csv"
FIELDS = ["checked_at", "marketplace", "id", "price", "currency", "in_stock", "title"]


def main(args: list[str]) -> None:
    if not args or len(args) % 2:
        sys.exit(f"usage: python price_tracker.py <marketplace> <id> [<marketplace> <id> ...]\nmarketplaces: {', '.join(MARKETPLACES)}")
    client = Apinoa()  # reads APINOA_API_KEY

    last: dict[tuple[str, str], str] = {}
    if os.path.exists(FILE):
        with open(FILE, newline="") as f:
            for row in csv.DictReader(f):
                last[(row["marketplace"], row["id"])] = row["price"]

    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        out = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            out.writeheader()
        for marketplace, product_id in zip(args[::2], args[1::2]):
            if marketplace not in MARKETPLACES:
                print(f'unknown marketplace "{marketplace}"', file=sys.stderr)
                continue
            try:
                product = getattr(client, marketplace).product(id=product_id).data
            except Exception as err:  # a failed call is not billed; the error says why
                print(f"{marketplace} {product_id}: {err}", file=sys.stderr)
                continue
            price = product.price.amount if product.price else None
            currency = product.price.currency if product.price else ""
            before = last.get((marketplace, product_id))
            change = "first check" if not before else ("unchanged" if float(before) == price else f"was {before}")
            print(f"{product.title}: {price if price is not None else 'no price'} {currency} ({change})")
            out.writerow({
                "checked_at": datetime.now(timezone.utc).isoformat(),
                "marketplace": marketplace,
                "id": product_id,
                "price": "" if price is None else price,
                "currency": currency,
                "in_stock": "" if product.in_stock is None else product.in_stock,
                "title": product.title,
            })


if __name__ == "__main__":
    main(sys.argv[1:])
