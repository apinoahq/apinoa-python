# Changelog

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
