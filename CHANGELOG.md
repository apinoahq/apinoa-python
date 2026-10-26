# Changelog

## 0.1.2

- TikTok `posts`, `profiles` and `groups`: `limit` is documented as 1–30, TikTok's own ceiling. A larger
  limit used to come back as a misleading 404 NOT_FOUND for a real account or hashtag; the API now answers
  it with a 400 that names `limit`. Comments still take up to 50.
- Walmart `reviews` with `page` works (it was a 400 over GET until the API fix of 2026-10-26; no SDK change
  was needed for it).

## 0.1.1

- Fix: on Python 3.9, `model_dump(mode="json")`, `model_dump_json()` and `.dict()` raised a TypeError
  for every response. They work on every supported Python now.

## 0.1.0

First release.
