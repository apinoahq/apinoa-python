# Changelog

## 0.1.5

Follows the API as of 2026-10-30:

- `google-shopping` `reviews`: `id` now says which products have reviews: only a product Google groups across stores, whose id is digits only. Another id answers `404 REVIEWS_NOT_FOUND`, with a message naming it.

## 0.1.4

Follows the API as of 2026-10-30:

- New operations: `GET /v1/app-store/search`, `GET /v1/app-store/app`, `GET /v1/app-store/reviews`, `GET /v1/baidu/search`, `GET /v1/baidu/suggestions`, `GET /v1/bing/search`, `GET /v1/bing/suggestions`, `POST /v1/chatgpt/answer`, `GET /v1/daum/search`, `GET /v1/daum/suggestions`, `GET /v1/duckduckgo/search`, `GET /v1/duckduckgo/suggestions`, `POST /v1/gemini/answer`, `GET /v1/google/search`, `GET /v1/google/suggestions`, `GET /v1/google/places`, `GET /v1/google/place`, `POST /v1/google-ai-mode/answer`, `POST /v1/google-aio/answer`, `GET /v1/google-play/search`, `GET /v1/google-play/app`, `GET /v1/google-play/reviews`, `GET /v1/google-shopping/search`, `GET /v1/google-shopping/product`, `GET /v1/google-shopping/reviews`, `GET /v1/google-trends/explore`, `GET /v1/google-trends/trending`, `GET /v1/naver/search`, `GET /v1/naver/suggestions`, `GET /v1/naver/places`, `GET /v1/naver/place`, `GET /v1/naver/reviews`, `POST /v1/naver-ai-brief/answer`, `POST /v1/naver-ai-tab/answer`, `GET /v1/seznam/search`, `GET /v1/seznam/suggestions`, `GET /v1/sogou/search`, `GET /v1/sogou/suggestions`, `GET /v1/tripadvisor/places`, `GET /v1/tripadvisor/place`, `GET /v1/tripadvisor/reviews`, `GET /v1/yahoo/search`, `GET /v1/yahoo/suggestions`, `GET /v1/yahoo-japan/search`, `GET /v1/yahoo-japan/suggestions`, `GET /v1/yandex/search`, `GET /v1/yandex/suggestions`, `GET /v1/yandex/places`, `GET /v1/yandex/place`, `GET /v1/yandex/reviews`.
- New type `Address`.
- New type `Answer`.
- New type `AnswerMention`.
- New type `AnswerResponse`.
- New type `App`.
- New type `AppResponse`.
- New type `AppReview`.
- New type `AppReviewsPage`.
- New type `AppReviewsPageResponse`.
- New type `AppsPage`.
- New type `AppsPageResponse`.
- New type `Block`.
- New type `Card`.
- New type `Citation`.
- New type `Conversation`.
- New type `Developer`.
- New type `Hours`.
- New type `PlaceReview`.
- New type `PlaceReviewsPage`.
- New type `PlaceReviewsPageResponse`.
- New type `PlacesPage`.
- New type `PlacesPageResponse`.
- New type `Price`.
- New type `Related`.
- New type `RelatedItem`.
- New type `Result`.
- New type `ResultsPage`.
- New type `ResultsPageResponse`.
- New type `SerpItem`.
- New type `SerpLink`.
- New type `SerpPlace`.
- New type `SerpPlaceResponse`.
- New type `Source`.
- New type `Suggestion`.
- New type `Suggestions`.
- New type `SuggestionsResponse`.
- New type `TrendPoint`.
- New type `TrendRegion`.
- New type `TrendingItem`.
- New type `TrendingPage`.
- New type `TrendingPageResponse`.
- New type `TrendsExplore`.
- New type `TrendsExploreResponse`.

## 0.1.3

Follows the API as of 2026-10-29:

- New type `CaptionTrack`.
- New type `MediaTag`.
- New type `ProtectionPlan`.
- `Account`: new `location`.
- `AccountPage`: no longer `total`.
- `AccountRef`: new `bio`, `bannerUrl`, `createdAt`, `links`, `private`, `category`, `location`.
- `Audio`: new `coverUrl`, `durationSec`, `original`, `album`, `ext`.
- `Broadcast`: new `ext`; no longer `scheduledAt`, `startedAt`, `endedAt`.
- `CategoryList`: new `ext`.
- `CategoryNode`: new `imageUrl`; no longer `productCount`.
- `Comment`: new `entities`, `edited`; no longer `moreReplies.ids`.
- `CommentPage`: new `order`, `post`.
- `DeliveryOption`: new `ext`; no longer `guaranteedDays`, `membership`, `tracking`.
- `FacetValue`: no longer `count`.
- `GroupPage`: new `order`; no longer `total`.
- `Job`: new `applyMethod`.
- `JobPage`: new `items.insights`.
- `LinkPreview`: new `ext`.
- `MediaVariant`: new `codec`, `sizeBytes`, `fps`, `quality`, `ext`.
- `MediaVideo`: new `ext`; no longer `creator`.
- `Mention`: new `ext`.
- `Offer`: new `shippingOptions`, `unitPrice`, `promotions`, `paymentOptions`.
- `Place`: new `type`, `ext`; no longer `region`, `postalCode`.
- `Poll`: new `ext`.
- `Post`: new `edited`; no longer `metrics.liveViewers`.
- `PostPage`: new `order`.
- `Product`: new `offersSummary.ext`, `highlights`, `protectionPlans`, `package.ext`; no longer `offersSummary.url`, `package.lengthCm`, `package.widthCm`, `package.heightCm`, `package.soldInLot`, `wholesale`, `included`.
- `Rating`: new `starCounts`.
- `Review`: new `authorAvatarUrl`, `unhelpfulCount`, `recommended`, `badges`, `syndicatedFrom`, `productId`, `productImageUrl`, `variantId`, `language`.
- `ReviewPage`: new `reviewSummary`, `reviewAspects`.
- `SearchItem`: new `subscriptionPrice`, `description`, `fulfilledBy`, `offersSummary.ext`, `offers`, `variants`; no longer `conditionNote`, `offersSummary.url`, `purchaseLimit`, `listedAt`.
- `SearchResult`: new `relatedSearches`, `ext`.
- `Seller`: new `logoUrl`, `productCount`; no longer `detailedRatings`.
- `ShippingOption`: new `ext`; no longer `guaranteedDays`, `membership`, `tracking`.
- `SocialMedia`: new `id`, `title`, `hasAudio`, `tags`, `captions`.
- `Variant`: new `name`, `images`; no longer `sku`, `bulkPrice`, `taxIncluded`.

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
