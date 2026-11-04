# Examples

Four small programs that use [`apinoa`](https://pypi.org/project/apinoa/). Copy one, change it, run it on
a schedule.

```bash
pip install -r requirements.txt
export APINOA_API_KEY=your_key   # https://apinoa.com/en/dashboard/api-keys
```

| File | What it does | Calls per run |
|---|---|---|
| [`price_tracker.py`](./price_tracker.py) | Reads products' prices on Amazon, Walmart, Shopify, AliExpress or TikTok Shop, keeps the history in `prices.csv` and says what changed | one per product |
| [`rank_tracker.py`](./rank_tracker.py) | Finds where a domain ranks for a query on Google, Bing, DuckDuckGo or Naver, and appends it to `ranks.csv` | one per engine and page |
| [`social_listening.py`](./social_listening.py) | Prints new Reddit, Threads or YouTube posts that mention a term, remembering what it has shown in `seen.json` | one per platform |
| [`ai_answer_monitor.py`](./ai_answer_monitor.py) | Asks ChatGPT, Gemini, Google AI Overviews or AI Mode a question and records whether your brand is named and which sources are cited | one per engine |

```bash
python price_tracker.py walmart 18256507800 shopify allbirds.com/products/mens-tree-runners
python rank_tracker.py "wool socks" example.com --engines google,bing --country US
python social_listening.py "your brand" --platforms reddit,youtube
python ai_answer_monitor.py "best wool socks for hiking" "Your Brand" --engines chatgpt,gemini
```

They run on Python 3.9 and later. Calls are billed to your key at the [normal rates](https://apinoa.com/pricing),
and a call that fails is not billed. Every response follows one schema per family, so code written for
one marketplace, engine or platform reads the others: see the [docs](https://apinoa.com/docs).
