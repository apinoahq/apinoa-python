# Reference
## AliExpress
<details><summary><code>client.aliexpress.<a href="src/apinoa/aliexpress/client.py">search</a>(...) -> SearchResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `SearchResult` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/aliexpress/search
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.aliexpress.search(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — Keywords. Required — AliExpress keyword search cannot be asked anything without words.
    
</dd>
</dl>

<dl>
<dd>

**category_id:** `typing.Optional[str]` — AliExpress category id; narrows the search.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Presentment currency.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — Presentment language.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — 1-based page number.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Results per page, 1-50.
    
</dd>
</dl>

<dl>
<dd>

**price_max:** `typing.Optional[float]` — Highest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**price_min:** `typing.Optional[float]` — Lowest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country (ISO 3166-1 alpha-2); sets shipping and availability.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[SearchAliexpressRequestSort]` — Result ordering, in the shared vocabulary.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.aliexpress.<a href="src/apinoa/aliexpress/client.py">browse</a>(...) -> SearchResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `SearchResult` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/aliexpress/browse
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.aliexpress.browse(
    category_id="categoryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `str` — AliExpress category id to list. Required — this is what is being browsed.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Presentment currency.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — Presentment language.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — 1-based page number.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Results per page, 1-50.
    
</dd>
</dl>

<dl>
<dd>

**price_max:** `typing.Optional[float]` — Highest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**price_min:** `typing.Optional[float]` — Lowest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country (ISO 3166-1 alpha-2); sets shipping and availability.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[BrowseAliexpressRequestSort]` — Result ordering, in the shared vocabulary.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.aliexpress.<a href="src/apinoa/aliexpress/client.py">categories</a>(...) -> CategoryListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `CategoryList` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/aliexpress/categories
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.aliexpress.categories()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `typing.Optional[str]` — Parent category id. Omit for the top-level categories.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.aliexpress.<a href="src/apinoa/aliexpress/client.py">image_search</a>(...) -> SearchResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `SearchResult` in `data`. Costs 1 unit. POST only, with a JSON body. Reference: https://apinoa.com/docs/api-reference/aliexpress/image-search
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.aliexpress.image_search(
    image={
        "key": "value"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image:** `typing.Dict[str, typing.Any]` — {contentType, data} with base64-encoded image bytes.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Presentment currency.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — Presentment language.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country (ISO 3166-1 alpha-2).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.aliexpress.<a href="src/apinoa/aliexpress/client.py">product</a>(...) -> ProductResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Product` in `data`. Costs 1 unit, up to 2 units. Reference: https://apinoa.com/docs/api-reference/aliexpress/product
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.aliexpress.product(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — AliExpress product id, as carried by a search item.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Presentment currency.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[ProductAliexpressRequestInclude]` — include=shipping adds `delivery`: the cheapest shipping cost and delivery days to `region` for the product's listed variant. Costs one more unit.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — Presentment language.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country (ISO 3166-1 alpha-2).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.aliexpress.<a href="src/apinoa/aliexpress/client.py">shipping</a>(...) -> ShippingQuoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `ShippingQuote` in `data`. Costs 1 unit, up to 2 units. Reference: https://apinoa.com/docs/api-reference/aliexpress/shipping
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.aliexpress.shipping(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — AliExpress product id.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Currency for the shipping fee. Default USD.
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `typing.Optional[int]` — How many units are shipped together. Default 1.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Destination country (ISO 3166-1 alpha-2). Default US.
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[str]` — The variant to quote: a variant `id` from the product, or a numeric sku id. Omit for the product's listed variant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Amazon
<details><summary><code>client.amazon.<a href="src/apinoa/amazon/client.py">search</a>(...) -> SearchResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `SearchResult` in `data`. Costs 1 unit, up to 2 units. Reference: https://apinoa.com/docs/api-reference/amazon/search
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.amazon.search(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — Keywords to search for. Required here; to search by picture use `image-search`.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — 1-based page number; each page is charged separately. There is no `pageSize` (Amazon fixes the count per page by keyword, 13-47 in practice) and no `cursor` — paging is by number.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[SearchAmazonRequestRegion]` — Which Amazon marketplace to query, by buyer country: US, CA, MX, BR, FR, IT, ES, NL, SE, TR, AE, SA, IN, JP, SG, AU. Defaults to US. Prices come back in that marketplace's own currency (JP in JPY, FR in EUR).
    
</dd>
</dl>

<dl>
<dd>

**category_id:** `typing.Optional[str]` — Narrow to one category, by the marketplace's own id. Opaque and per-marketplace; take it from Product.category[].id or from a result's `facets`.
    
</dd>
</dl>

<dl>
<dd>

**brands:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Brand names as Amazon spells them, e.g. brands=Nike,Adidas. A call that uses `brands` costs 2 units instead of 1. Not available on amazon.fr (`region=FR`).
    
</dd>
</dl>

<dl>
<dd>

**facets:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Narrowings taken from a result's `facets`, e.g. facets=Color:Black. A call that uses `facets` costs 2 units instead of 1. Not available on amazon.fr (`region=FR`).
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Expansions that cost more than the default answer, e.g. include=facets.
    
</dd>
</dl>

<dl>
<dd>

**price_min:** `typing.Optional[float]` — Lowest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**price_max:** `typing.Optional[float]` — Highest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**rating_min:** `typing.Optional[float]` — `4` only. Amazon's rating filter offers exactly one threshold, "4 Stars & Up"; any other value is a 400 rather than a silently different search. Not available on amazon.fr (`region=FR`).
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[SearchAmazonRequestSort]` — Result ordering: `best_match`, `price_asc`, `price_desc`, `newly_listed` or `avg_review`. Defaults to `best_match`, Amazon's own relevance ordering.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.amazon.<a href="src/apinoa/amazon/client.py">image_search</a>(...) -> SearchResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `SearchResult` in `data`. Costs 1 unit, up to 2 units. POST only, with a JSON body. Reference: https://apinoa.com/docs/api-reference/amazon/image-search
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment
from apinoa.amazon import ImageSearchAmazonRequestImage

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.amazon.image_search(
    image=ImageSearchAmazonRequestImage(
        content_type="contentType",
        data="data",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image:** `ImageSearchAmazonRequestImage` — The picture to search by: `{contentType, data}` with `data` base64-encoded. POST only — a base64 image is tens of kilobytes and a URL caps out around 8 KB.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Optional words that narrow the visual matches, e.g. the product type. Supplying it is usually much more precise.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — 1-based page number over the visual matches, about 48 per page; each page is charged separately. No `pageSize` and no `cursor`.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[ImageSearchAmazonRequestRegion]` — Which Amazon marketplace to query, by buyer country: US, CA, MX, BR, FR, IT, ES, NL, SE, TR, AE, SA, IN, JP, SG, AU. Defaults to US. Prices come back in that marketplace's own currency (JP in JPY, FR in EUR).
    
</dd>
</dl>

<dl>
<dd>

**category_id:** `typing.Optional[str]` — Narrow to one category, by the marketplace's own id. Opaque and per-marketplace; take it from Product.category[].id or from a result's `facets`.
    
</dd>
</dl>

<dl>
<dd>

**price_min:** `typing.Optional[float]` — Lowest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**price_max:** `typing.Optional[float]` — Highest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**rating_min:** `typing.Optional[float]` — `4` only. Amazon's rating filter offers exactly one threshold, "4 Stars & Up"; any other value is a 400 rather than a silently different search. Not available on amazon.fr (`region=FR`).
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ImageSearchAmazonRequestSort]` — Result ordering: `best_match`, `price_asc`, `price_desc`, `newly_listed` or `avg_review`. Defaults to `best_match`, Amazon's own relevance ordering.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.amazon.<a href="src/apinoa/amazon/client.py">browse</a>(...) -> SearchResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `SearchResult` in `data`. Costs 1 unit, up to 2 units. Reference: https://apinoa.com/docs/api-reference/amazon/browse
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.amazon.browse(
    category_id="categoryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `str` — REQUIRED. An Amazon browse NODE — the digits from a category URL, e.g. `172541`. The department slugs `categories` returns at its root (`electronics`) are NOT browse nodes and are refused with `CATEGORY_NOT_BROWSABLE`: call `categories` with the slug to get its child nodes and browse one of those.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — 1-based page number; each page is charged separately. There is no `pageSize` (Amazon fixes the count per page, 13-47 in practice) and no `cursor` — paging is by number.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[BrowseAmazonRequestRegion]` — Which Amazon marketplace to query, by buyer country: US, CA, MX, BR, FR, IT, ES, NL, SE, TR, AE, SA, IN, JP, SG, AU. Defaults to US. Prices come back in that marketplace's own currency (JP in JPY, FR in EUR).
    
</dd>
</dl>

<dl>
<dd>

**brands:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Brand names as Amazon spells them, e.g. brands=Nike,Adidas. A call that uses `brands` costs 2 units instead of 1. Not available on amazon.fr (`region=FR`).
    
</dd>
</dl>

<dl>
<dd>

**facets:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Narrowings taken from a result's `facets`, e.g. facets=Color:Black. A call that uses `facets` costs 2 units instead of 1. Not available on amazon.fr (`region=FR`).
    
</dd>
</dl>

<dl>
<dd>

**price_min:** `typing.Optional[float]` — Lowest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**price_max:** `typing.Optional[float]` — Highest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**rating_min:** `typing.Optional[float]` — `4` only. Amazon's rating filter offers exactly one threshold, "4 Stars & Up"; any other value is a 400 rather than a silently different search. Not available on amazon.fr (`region=FR`).
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[BrowseAmazonRequestSort]` — Result ordering: `best_match`, `price_asc`, `price_desc`, `newly_listed` or `avg_review`. Defaults to `best_match`, Amazon's own relevance ordering.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.amazon.<a href="src/apinoa/amazon/client.py">categories</a>(...) -> CategoryListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `CategoryList` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/amazon/categories
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.amazon.categories()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `typing.Optional[str]` — Omit for the 40 departments; give a browse node (`172541`) or a department slug (`electronics`) to list that category's children. This is the one endpoint that takes either kind of id.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[CategoriesAmazonRequestRegion]` — Which Amazon marketplace to query, by buyer country: US, CA, MX, BR, FR, IT, ES, NL, SE, TR, AE, SA, IN, JP, SG, AU. Defaults to US. Prices come back in that marketplace's own currency (JP in JPY, FR in EUR).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.amazon.<a href="src/apinoa/amazon/client.py">product</a>(...) -> ProductResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Product` in `data`. Costs 2 units, up to 32 units. Reference: https://apinoa.com/docs/api-reference/amazon/product
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.amazon.product(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The marketplace's own product id, as carried by a search item.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — `offers` · `offers:5` · `offers:all` — the enumerated competing-seller offers, which are fetched separately and so opt-in. Depth counts pages of offers (10 offers each) and each page is charged; `all` walks to the end, capped at 30 pages.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[ProductAmazonRequestRegion]` — Which Amazon marketplace to query, by buyer country: US, CA, MX, BR, FR, IT, ES, NL, SE, TR, AE, SA, IN, JP, SG, AU. Defaults to US. Prices come back in that marketplace's own currency (JP in JPY, FR in EUR).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Instagram
<details><summary><code>client.instagram.<a href="src/apinoa/instagram/client.py">profile</a>(...) -> AccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Account` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/instagram/profile
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.instagram.profile()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Creator @handle (with or without @), or the profile URL.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Attach from the same page, at no extra cost: posts (the creator's latest posts, ext.posts).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.instagram.<a href="src/apinoa/instagram/client.py">post</a>(...) -> PostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Post` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/instagram/post
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.instagram.post()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — Post shortcode, or the post URL (…/p/<code>/, …/reel/<code>/, …/tv/<code>/).
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Attach from the same page, at no extra cost: comments (the first comments, ext.comments), authorPosts (the author's other recent posts, ext.authorPosts).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.instagram.<a href="src/apinoa/instagram/client.py">posts</a>(...) -> PostPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `PostPage` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/instagram/posts
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.instagram.posts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Creator @handle (with or without @), or the profile URL.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[PostsInstagramRequestType]` — username: the creator's posts (default) or reels.
    
</dd>
</dl>

<dl>
<dd>

**hashtag:** `typing.Optional[str]` — Top posts under a hashtag: with or without #, or its page URL.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — Posts at a location: numeric location id or URL (…/explore/locations/<id>/). One page: Instagram shows the rest only to signed-in users.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.instagram.<a href="src/apinoa/instagram/client.py">comments</a>(...) -> CommentPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `CommentPage` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/instagram/comments
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.instagram.comments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**post:** `typing.Optional[str]` — The post's comments: shortcode or URL.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[CommentsInstagramRequestSort]` — recent (newest first) — the only order Instagram serves logged-out visitors.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.instagram.<a href="src/apinoa/instagram/client.py">group</a>(...) -> GroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Group` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/instagram/group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.instagram.group()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**hashtag:** `typing.Optional[str]` — A hashtag: with or without #, or its page URL.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — A location: numeric id or URL (…/explore/locations/<id>/).
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Attach from the same page, at no extra cost: posts (the tag's top posts / the location's posts, ext.posts).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.instagram.<a href="src/apinoa/instagram/client.py">groups</a>(...) -> GroupPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `GroupPage` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/instagram/groups
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.instagram.groups()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Creator @handle (with or without @), or the profile URL.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GroupsInstagramRequestType]` — highlights (a creator's highlight reels).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LinkedIn
<details><summary><code>client.linkedin.<a href="src/apinoa/linkedin/client.py">profile</a>(...) -> AccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Account` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/linkedin/profile
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.linkedin.profile()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Person vanity handle (with or without in/, e.g. williamhgates), or the profile URL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.linkedin.<a href="src/apinoa/linkedin/client.py">post</a>(...) -> PostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Post` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/linkedin/post
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.linkedin.post()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — Activity id, urn:li:activity:<id>, or the post URL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.linkedin.<a href="src/apinoa/linkedin/client.py">posts</a>(...) -> PostPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `PostPage` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/linkedin/posts
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.linkedin.posts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Person vanity handle (with or without in/, e.g. williamhgates), or the profile URL.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[str]` — Company vanity name (with or without company/, e.g. microsoft), or the company URL.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Most posts to return (LinkedIn shows the most recent few).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.linkedin.<a href="src/apinoa/linkedin/client.py">comments</a>(...) -> CommentPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `CommentPage` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/linkedin/comments
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.linkedin.comments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**post:** `typing.Optional[str]` — The post's comments: activity id, urn:li:activity:<id>, or URL.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Most comments to return (LinkedIn shows a post's top few).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.linkedin.<a href="src/apinoa/linkedin/client.py">group</a>(...) -> GroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Group` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/linkedin/group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.linkedin.group()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company:** `typing.Optional[str]` — Company vanity name (with or without company/, e.g. microsoft), or the company URL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.linkedin.<a href="src/apinoa/linkedin/client.py">job</a>(...) -> JobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Job` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/linkedin/job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.linkedin.job()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — Numeric job id, urn:li:jobPosting:<id>, or the job URL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.linkedin.<a href="src/apinoa/linkedin/client.py">jobs</a>(...) -> JobPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `JobPage` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/linkedin/jobs
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.linkedin.jobs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[str]` — Job search keywords (e.g. software engineer).
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — Location name (e.g. United States). Default: worldwide.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Reddit
<details><summary><code>client.reddit.<a href="src/apinoa/reddit/client.py">profile</a>(...) -> AccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Account` in `data`. Costs 1 unit, up to 2 units. Reference: https://apinoa.com/docs/api-reference/reddit/profile
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.reddit.profile()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Username, with or without u/, or the profile URL.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Extra reads to attach under `ext`: trophies (+1 unit).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reddit.<a href="src/apinoa/reddit/client.py">profiles</a>(...) -> AccountPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `AccountPage` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/reddit/profiles
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.reddit.profiles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[str]` — Keywords to search accounts for.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Items per page, 1–100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reddit.<a href="src/apinoa/reddit/client.py">post</a>(...) -> PostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Post` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/reddit/post
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.reddit.post()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — Post id (base36), fullname (t3_…), or the post URL (reddit.com, old.reddit.com, redd.it).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reddit.<a href="src/apinoa/reddit/client.py">posts</a>(...) -> PostPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `PostPage` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/reddit/posts
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.reddit.posts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — A user's posts: username (with or without u/) or profile URL.
    
</dd>
</dl>

<dl>
<dd>

**community:** `typing.Optional[str]` — A community's posts: name (with or without r/) or URL. With `query`, narrows the search to it.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search posts by keyword.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Specific posts: ids, fullnames (t3_…) or URLs, 1–100 in one call.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[PostsRedditRequestSort]` — Order. username: new, hot, top, controversial · community: hot, new, top, rising, controversial · query: relevance, hot, top, new, comments · default feed: hot, new, top, rising.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[PostsRedditRequestPeriod]` — Time window for sort top or controversial: hour, day, week, month, year or all.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Default feed only: the country whose popular feed to read (ISO alpha-2).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Items per page, 1–100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reddit.<a href="src/apinoa/reddit/client.py">comments</a>(...) -> CommentPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `CommentPage` in `data`. Costs 1 unit, up to 3 units. Reference: https://apinoa.com/docs/api-reference/reddit/comments
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.reddit.comments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**post:** `typing.Optional[str]` — A post's comments: post id, fullname (t3_…) or URL.
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` — With `post`: the comment whose replies to load (base36 id or t1_ fullname) — e.g. one whose `moreReplies` says replies were held back.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — A user's comments: username or profile URL.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[CommentsRedditRequestSort]` — Order. post: confidence (Reddit's 'best'), top, new, controversial, old, qa · username: new, hot, top, controversial.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[CommentsRedditRequestPeriod]` — Time window for sort top or controversial: hour, day, week, month, year or all.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Items per page, 1–100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reddit.<a href="src/apinoa/reddit/client.py">group</a>(...) -> GroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Group` in `data`. Costs 1 unit, up to 2 units. Reference: https://apinoa.com/docs/api-reference/reddit/group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.reddit.group()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**community:** `typing.Optional[str]` — Community name (with or without r/) or URL.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Extra reads to attach under `ext`: rules (+1 unit). The community's style is always in `ext.style` (it comes with the community), so `style` is accepted and free.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reddit.<a href="src/apinoa/reddit/client.py">groups</a>(...) -> GroupPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `GroupPage` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/reddit/groups
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.reddit.groups()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search communities by keyword.
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` — Autocomplete: communities whose name starts with this (fast, one page).
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — The communities a user is active in: username or profile URL.
    
</dd>
</dl>

<dl>
<dd>

**include_nsfw:** `typing.Optional[bool]` — prefix only: include over-18 communities.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Items per page, 1–100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Shopify
<details><summary><code>client.shopify.<a href="src/apinoa/shopify/client.py">search</a>(...) -> SearchResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `SearchResult` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/shopify/search
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.shopify.search(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — Keywords to search for. Required: Shopify search always needs a keyword, which is also why Shopify has no keyword-less `browse`.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque; comes from the previous response and carries the page index. Shopify pages by cursor rather than by number — this is the only paging knob, and `page` is refused by name.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country as ISO 3166-1 alpha-2; sets availability, shipping and price.
    
</dd>
</dl>

<dl>
<dd>

**category_id:** `typing.Optional[str]` — Narrow to one category, by the marketplace's own id. Opaque and per-marketplace; take it from Product.category[].id or from a result's `facets`.
    
</dd>
</dl>

<dl>
<dd>

**price_min:** `typing.Optional[float]` — Lowest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**price_max:** `typing.Optional[float]` — Highest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**rating_min:** `typing.Optional[float]` — Lowest average star rating to return, on the marketplace's own 0-5 scale.
    
</dd>
</dl>

<dl>
<dd>

**condition:** `typing.Optional[SearchShopifyRequestCondition]` — Item condition: `new` or `used`. `refurbished` is refused by name rather than folded into `used` — the catalog sells new and secondhand, and those are different claims.
    
</dd>
</dl>

<dl>
<dd>

**in_stock:** `typing.Optional[bool]` — Only listings the marketplace reports as purchasable now.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shopify.<a href="src/apinoa/shopify/client.py">image_search</a>(...) -> SearchResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `SearchResult` in `data`. Costs 1 unit. POST only, with a JSON body. Reference: https://apinoa.com/docs/api-reference/shopify/image-search
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment
from apinoa.shopify import ImageSearchShopifyRequestImage

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.shopify.image_search(
    image=ImageSearchShopifyRequestImage(
        content_type="contentType",
        data="data",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image:** `ImageSearchShopifyRequestImage` — Base64 image input for visual search; the image is the anchor and `query` narrows it — the reverse of `search`. Up to ~6MB of base64; supported types are jpeg, png, webp, gif and avif.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Optional text that refines the image — the reverse of `search`, where the query anchors the result. For example, a sneaker photo with `query=wool` returns wool sneakers rather than any sneaker of that shape.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque; comes from the previous response and carries the page index. Shopify pages by cursor rather than by number — this is the only paging knob, and `page` is refused by name.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country as ISO 3166-1 alpha-2; sets availability, shipping and price.
    
</dd>
</dl>

<dl>
<dd>

**category_id:** `typing.Optional[str]` — Narrow to one category, by the marketplace's own id. Opaque and per-marketplace; take it from Product.category[].id or from a result's `facets`.
    
</dd>
</dl>

<dl>
<dd>

**price_min:** `typing.Optional[float]` — Lowest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**price_max:** `typing.Optional[float]` — Highest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**rating_min:** `typing.Optional[float]` — Lowest average star rating to return, on the marketplace's own 0-5 scale.
    
</dd>
</dl>

<dl>
<dd>

**condition:** `typing.Optional[ImageSearchShopifyRequestCondition]` — Item condition: `new` or `used`. `refurbished` is refused by name rather than folded into `used` — the catalog sells new and secondhand, and those are different claims.
    
</dd>
</dl>

<dl>
<dd>

**in_stock:** `typing.Optional[ImageSearchShopifyRequestInStock]` — Only listings the marketplace reports as purchasable now.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shopify.<a href="src/apinoa/shopify/client.py">catalog</a>(...) -> SearchResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `SearchResult` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/shopify/catalog
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.shopify.catalog(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The store: its host (comfrt.com) or any URL on it — a product, collection or home page link.
    
</dd>
</dl>

<dl>
<dd>

**collection:** `typing.Optional[str]` — Only this collection: its handle (best-sellers) or its URL. Omitted means the whole store — unless `id` is itself a collection page link, which lists that collection.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — 1-based page number.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Products per page, 1–250 (default 50).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The previous page's `cursor`. Pass it for the next page; it also carries the store's total forward.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Presentment currency, ISO 4217.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country as ISO 3166-1 alpha-2; sets availability, shipping and price.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shopify.<a href="src/apinoa/shopify/client.py">product</a>(...) -> ProductResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Product` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/shopify/product
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.shopify.product(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A Shopify id rather than a global identifier: the composite `shop/handle`, e.g. us.giesswein.com/wool-sneaker-women. A search item's `id` is already in this form, and a full product URL is accepted too.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Presentment currency, ISO 4217.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country as ISO 3166-1 alpha-2; sets availability, shipping and price.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shopify.<a href="src/apinoa/shopify/client.py">reviews</a>(...) -> ReviewPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `ReviewPage` in `data`. Costs 1 unit, up to 7 units. Reference: https://apinoa.com/docs/api-reference/shopify/reviews
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.shopify.reviews(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The composite Shopify `shop/handle` — the same id `product` takes, not a global identifier. This is the one Shopify operation whose cost varies: a first page can cost more than 1, while a page fetched with `cursor` costs 1.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — 1-based starting page. Not every shop supports jumping to a page number; `cursor` works on every shop, so prefer it for paging.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous response; the only paging knob that works on every shop, and it wins if `page` is sent too. A page fetched with a cursor costs 1.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Threads
<details><summary><code>client.threads.<a href="src/apinoa/threads/client.py">profile</a>(...) -> AccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Account` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/threads/profile
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.threads.profile()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Creator @handle (with or without @), or the profile URL.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Numeric Threads user id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.threads.<a href="src/apinoa/threads/client.py">post</a>(...) -> PostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Post` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/threads/post
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.threads.post()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — Post shortcode, or the post URL (…/@user/post/<code> or …/t/<code>).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.threads.<a href="src/apinoa/threads/client.py">posts</a>(...) -> PostPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `PostPage` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/threads/posts
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.threads.posts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Creator @handle (with or without @), or the profile URL.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[PostsThreadsRequestType]` — username: the creator's threads (default), reposts or replies.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search posts by keyword (one page).
    
</dd>
</dl>

<dl>
<dd>

**hashtag:** `typing.Optional[str]` — Posts for a topic tag, with or without # (one page). Threads often answers a tag as a keyword match over post text and topic names; the page's `ext.matchedBy` says `tag` or `keyword`.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[PostsThreadsRequestSort]` — query only: top (default) or recent.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.threads.<a href="src/apinoa/threads/client.py">comments</a>(...) -> CommentPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `CommentPage` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/threads/comments
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.threads.comments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**post:** `typing.Optional[str]` — The post's replies: shortcode or URL.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[CommentsThreadsRequestSort]` — top (default) or recent.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TikTok
<details><summary><code>client.tiktok.<a href="src/apinoa/tiktok/client.py">profile</a>(...) -> AccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Account` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/tiktok/profile
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.tiktok.profile()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Creator @handle (with or without @), or the profile URL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tiktok.<a href="src/apinoa/tiktok/client.py">profiles</a>(...) -> AccountPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `AccountPage` in `data`. Costs 1 unit, up to 2 units. Reference: https://apinoa.com/docs/api-reference/tiktok/profiles
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.tiktok.profiles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Creator @handle (with or without @), or the profile URL.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Creator secUid. Pass it instead of a username to save the lookup (1 unit instead of 2).
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ProfilesTiktokRequestType]` — Which list: followers or following.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Items per page, 1–30.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tiktok.<a href="src/apinoa/tiktok/client.py">post</a>(...) -> PostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Post` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/tiktok/post
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.tiktok.post()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — Numeric video id, or the video URL / share link (vm.tiktok.com/…).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tiktok.<a href="src/apinoa/tiktok/client.py">posts</a>(...) -> PostPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `PostPage` in `data`. Costs 1 unit, up to 2 units. Reference: https://apinoa.com/docs/api-reference/tiktok/posts
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.tiktok.posts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Creator @handle (with or without @), or the profile URL.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Creator secUid. Pass it instead of a username to save the lookup (1 unit instead of 2).
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[PostsTiktokRequestType]` — username/userId: the creator's posts (default), reposts or likes.
    
</dd>
</dl>

<dl>
<dd>

**hashtag:** `typing.Optional[str]` — Videos under a hashtag: its name, or its numeric id (saves the lookup). A hashtag that is itself a number takes its # (#2024).
    
</dd>
</dl>

<dl>
<dd>

**sound:** `typing.Optional[str]` — Videos using a sound: sound id or URL (…/music/-<id>).
    
</dd>
</dl>

<dl>
<dd>

**playlist:** `typing.Optional[str]` — Videos in a playlist: id or URL (…/playlist/-<id>).
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` — Default feed only: explore category id (default 120).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Items per page, 1–30.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tiktok.<a href="src/apinoa/tiktok/client.py">comments</a>(...) -> CommentPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `CommentPage` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/tiktok/comments
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.tiktok.comments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**post:** `typing.Optional[str]` — The video's comments: numeric video id or URL.
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` — With `post`: the comment whose replies to load (its id).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Items per page, 1–50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tiktok.<a href="src/apinoa/tiktok/client.py">group</a>(...) -> GroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Group` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/tiktok/group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.tiktok.group()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**hashtag:** `typing.Optional[str]` — A hashtag: its name, or its numeric id. A hashtag that is itself a number takes its # (#2024).
    
</dd>
</dl>

<dl>
<dd>

**sound:** `typing.Optional[str]` — A sound: id or URL (…/music/-<id>).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tiktok.<a href="src/apinoa/tiktok/client.py">groups</a>(...) -> GroupPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `GroupPage` in `data`. Costs 1 unit, up to 2 units. Reference: https://apinoa.com/docs/api-reference/tiktok/groups
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.tiktok.groups()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Creator @handle (with or without @), or the profile URL.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Creator secUid. Pass it instead of a username to save the lookup (1 unit instead of 2).
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GroupsTiktokRequestType]` — playlists (the only list TikTok has).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Items per page, 1–30.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tiktok.<a href="src/apinoa/tiktok/client.py">media</a>(...) -> MediaFileResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `MediaFile` in `data`. Costs 2 units. Reference: https://apinoa.com/docs/api-reference/tiktok/media
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.tiktok.media()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**post:** `typing.Optional[str]` — The post whose file to download: numeric id or URL. A video gives its MP4, a photo post one picture.
    
</dd>
</dl>

<dl>
<dd>

**index:** `typing.Optional[int]` — Photo posts: which picture, 1-based (default 1).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TikTok Shop
<details><summary><code>client.tiktokshop.<a href="src/apinoa/tiktokshop/client.py">search</a>(...) -> SearchResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `SearchResult` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/tiktokshop/search
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.tiktokshop.search(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — Keywords to search for.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country as ISO 3166-1 alpha-2; sets availability, shipping and price.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tiktokshop.<a href="src/apinoa/tiktokshop/client.py">browse</a>(...) -> SearchResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `SearchResult` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/tiktokshop/browse
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.tiktokshop.browse(
    category_id="categoryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `str` — REQUIRED. The category to list, by the marketplace's own id.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country as ISO 3166-1 alpha-2; sets availability, shipping and price.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tiktokshop.<a href="src/apinoa/tiktokshop/client.py">categories</a>(...) -> CategoryListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `CategoryList` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/tiktokshop/categories
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.tiktokshop.categories()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `typing.Optional[str]` — Omit for the root departments; give a category id to list its children.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country as ISO 3166-1 alpha-2; sets availability, shipping and price.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tiktokshop.<a href="src/apinoa/tiktokshop/client.py">catalog</a>(...) -> SearchResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `SearchResult` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/tiktokshop/catalog
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.tiktokshop.catalog(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The store, by the marketplace's own id (on Shopify: its host or any URL on it).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The previous page's `cursor`, for the next 30 products.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country as ISO 3166-1 alpha-2; sets availability, shipping and price.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tiktokshop.<a href="src/apinoa/tiktokshop/client.py">product</a>(...) -> ProductResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Product` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/tiktokshop/product
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.tiktokshop.product(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The marketplace's own product id, as carried by a search item.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country as ISO 3166-1 alpha-2; sets availability, shipping and price.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tiktokshop.<a href="src/apinoa/tiktokshop/client.py">reviews</a>(...) -> ReviewPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `ReviewPage` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/tiktokshop/reviews
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.tiktokshop.reviews(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The product whose reviews to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Walmart
<details><summary><code>client.walmart.<a href="src/apinoa/walmart/client.py">search</a>(...) -> SearchResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `SearchResult` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/walmart/search
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.walmart.search(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — Keywords to search for. Required: image search is not available on Walmart, so a keyword query is the only way to search.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — 1-based results page. There is no `pageSize` — the results page is server-fixed at about 50 organic items — and no `cursor`, since paging here is by number.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country as ISO 3166-1 alpha-2; sets availability, shipping and price.
    
</dd>
</dl>

<dl>
<dd>

**category_id:** `typing.Optional[str]` — Narrow to one category, by the marketplace's own id. Opaque and per-marketplace; take it from Product.category[].id or from a result's `facets`.
    
</dd>
</dl>

<dl>
<dd>

**price_min:** `typing.Optional[float]` — Lowest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**price_max:** `typing.Optional[float]` — Highest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**brands:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Brand names as the marketplace spells them, e.g. brands=Nike,Adidas.
    
</dd>
</dl>

<dl>
<dd>

**rating_min:** `typing.Optional[float]` — Lowest average star rating to return, on the marketplace's own 0-5 scale.
    
</dd>
</dl>

<dl>
<dd>

**facets:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Narrowings taken from a result's `facets`, e.g. facets=Color:Black. The escape hatch for filters the typed vocabulary has no word for; prefer a typed parameter where one exists.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[SearchWalmartRequestSort]` — Result ordering: `best_match`, `price_asc`, `price_desc`, `newly_listed` or `best_seller`. Defaults to `best_match`, Walmart's own relevance ordering.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.walmart.<a href="src/apinoa/walmart/client.py">browse</a>(...) -> SearchResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `SearchResult` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/walmart/browse
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.walmart.browse(
    category_id="categoryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `str` — REQUIRED. The underscore-joined chain from a Walmart category URL, e.g. 3944_133251_1095191_1230614_1230478. A bare department or leaf id is refused with CATEGORY_NOT_BROWSABLE — use `categories` to walk down to a chain.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — 1-based results page. There is no `pageSize` — the results page is server-fixed at about 50 organic items — and no `cursor`, since paging here is by number.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country as ISO 3166-1 alpha-2; sets availability, shipping and price.
    
</dd>
</dl>

<dl>
<dd>

**price_min:** `typing.Optional[float]` — Lowest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**price_max:** `typing.Optional[float]` — Highest price to return, in decimal major units.
    
</dd>
</dl>

<dl>
<dd>

**brands:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Brand names as the marketplace spells them, e.g. brands=Nike,Adidas.
    
</dd>
</dl>

<dl>
<dd>

**rating_min:** `typing.Optional[float]` — Lowest average star rating to return, on the marketplace's own 0-5 scale.
    
</dd>
</dl>

<dl>
<dd>

**facets:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Narrowings taken from a result's `facets`, e.g. facets=Color:Black. The escape hatch for filters the typed vocabulary has no word for; prefer a typed parameter where one exists.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[BrowseWalmartRequestSort]` — Result ordering: `best_match`, `price_asc`, `price_desc`, `newly_listed` or `best_seller`. Defaults to `best_match`, Walmart's own relevance ordering.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.walmart.<a href="src/apinoa/walmart/client.py">categories</a>(...) -> CategoryListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `CategoryList` in `data`. Costs 1 unit, up to 2 units. Reference: https://apinoa.com/docs/api-reference/walmart/categories
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.walmart.categories()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `typing.Optional[str]` — Omit for the 42 departments; give a bare department id (`4171`) or an underscore chain to list that category's children. Unlike `browse`, a bare id is accepted here — descending from one is how a client reaches the chains `browse` takes.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country as ISO 3166-1 alpha-2; sets availability, shipping and price.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.walmart.<a href="src/apinoa/walmart/client.py">product</a>(...) -> ProductResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Product` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/walmart/product
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.walmart.product(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Walmart's `usItemId`, all digits, as carried by a search item — chain straight in.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Buyer country as ISO 3166-1 alpha-2; sets availability, shipping and price.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.walmart.<a href="src/apinoa/walmart/client.py">reviews</a>(...) -> ReviewPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `ReviewPage` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/walmart/reviews
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.walmart.reviews(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Walmart's `usItemId`, all digits, as carried by a search item.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — 1-based review page; Walmart returns 10 reviews per page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## X
<details><summary><code>client.x.<a href="src/apinoa/x/client.py">profile</a>(...) -> AccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Account` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/x/profile
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.x.profile()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — @handle (with or without @), or the profile URL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.x.<a href="src/apinoa/x/client.py">post</a>(...) -> PostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Post` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/x/post
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.x.post()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — Numeric post id, or the post URL (x.com/<handle>/status/<id>).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.x.<a href="src/apinoa/x/client.py">posts</a>(...) -> PostPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `PostPage` in `data`. Costs 1 unit, up to 2 units. Reference: https://apinoa.com/docs/api-reference/x/posts
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.x.posts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — @handle (with or without @), or the profile URL.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Numeric user id. Pass it instead of a username to save the lookup.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Items per page, 1–100 — a hint only: X decides the page size (about 20, or ~100 for the most-liked list).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.x.<a href="src/apinoa/x/client.py">group</a>(...) -> GroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Group` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/x/group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.x.group()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**community:** `typing.Optional[str]` — Numeric community id, or the community URL (x.com/i/communities/<id>).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## YouTube
<details><summary><code>client.youtube.<a href="src/apinoa/youtube/client.py">profile</a>(...) -> AccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Account` in `data`. Costs 1 unit, up to 3 units. Reference: https://apinoa.com/docs/api-reference/youtube/profile
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.youtube.profile()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Channel @handle (with or without @), or the channel URL (/@handle, /channel/UC…, /c/…, /user/…).
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Channel id (UC…).
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — about: also read the channel's About panel — join date (createdAt), exact video count, total views, country and every link (+1 unit).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.youtube.<a href="src/apinoa/youtube/client.py">profiles</a>(...) -> AccountPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `AccountPage` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/youtube/profiles
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.youtube.profiles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search channels by keyword.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.youtube.<a href="src/apinoa/youtube/client.py">post</a>(...) -> PostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Post` in `data`. Costs 1 unit. Reference: https://apinoa.com/docs/api-reference/youtube/post
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.youtube.post()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — Video id (11 chars), or the video URL (watch?v=…, youtu.be/…, /shorts/…).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.youtube.<a href="src/apinoa/youtube/client.py">posts</a>(...) -> PostPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `PostPage` in `data`. Costs 1 unit, up to 2 units. Reference: https://apinoa.com/docs/api-reference/youtube/posts
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.youtube.posts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Channel @handle (with or without @), or the channel URL (/@handle, /channel/UC…, /c/…, /user/…).
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Channel id (UC…).
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search videos by keyword.
    
</dd>
</dl>

<dl>
<dd>

**hashtag:** `typing.Optional[str]` — Videos under a hashtag, with or without #.
    
</dd>
</dl>

<dl>
<dd>

**related_to:** `typing.Optional[str]` — A video id or URL; returns the videos YouTube recommends beside it.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[PostsYoutubeRequestType]` — username/userId: which channel tab — videos (default), shorts, live or community · query: videos (default) or shorts.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Default feed only: the country whose trending feed to read (ISO alpha-2, default US).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.youtube.<a href="src/apinoa/youtube/client.py">comments</a>(...) -> CommentPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `CommentPage` in `data`. Costs 1 unit, up to 2 units. Reference: https://apinoa.com/docs/api-reference/youtube/comments
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.youtube.comments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**post:** `typing.Optional[str]` — The video's comments: video id or URL.
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` — A comment's replies: the comment's `moreReplies.cursor`.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.youtube.<a href="src/apinoa/youtube/client.py">groups</a>(...) -> GroupPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `GroupPage` in `data`. Costs 1 unit, up to 2 units. Reference: https://apinoa.com/docs/api-reference/youtube/groups
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.youtube.groups()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Channel @handle (with or without @), or the channel URL (/@handle, /channel/UC…, /c/…, /user/…).
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Channel id (UC…).
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GroupsYoutubeRequestType]` — playlists (a channel's playlists).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page's `cursor`. Pass it alone for the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Marketplaces
<details><summary><code>client.marketplaces.<a href="src/apinoa/marketplaces/client.py">list</a>() -> CatalogResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public: works without a key. Reference: https://apinoa.com/docs/api-reference/marketplaces
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.marketplaces.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Image translate
<details><summary><code>client.image_translate.<a href="src/apinoa/image_translate/client.py">translate</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces the text inside a product image with a translation, keeping weight, colours, layout and badge backdrops. Returns the translated JPEG, or with render=false the cleaned image and every text region as JSON. Most calls take 1.5–3 s; allow up to 300 s. Reference: https://apinoa.com/docs/api-reference/image-translate/translate
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.image_translate.translate(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_language:** `TranslateImageTranslateRequestSourceLanguage` — The text's language: ch, zh, zh-CN, zh-TW, chinese_cht, ja, japan, en, or auto.
    
</dd>
</dl>

<dl>
<dd>

**target_language:** `str` — The language to translate into (ISO 639-style code, e.g. ko, en, ja, zh-CN).
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — The image as raw bytes (not JSON, not base64). JPEG, PNG or WebP, up to 20 MB and 8192 × 8192 px.
    
</dd>
</dl>

<dl>
<dd>

**font:** `typing.Optional[str]` — A value from allFonts in supported-fonts, or user/<id> for an uploaded font. Default Pretendard.
    
</dd>
</dl>

<dl>
<dd>

**font_weight:** `typing.Optional[TranslateImageTranslateRequestFontWeight]` — auto matches each region's original weight. Default ExtraBold.
    
</dd>
</dl>

<dl>
<dd>

**render:** `typing.Optional[bool]` — true (default) returns the finished image; false returns the regions as JSON.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.image_translate.<a href="src/apinoa/image_translate/client.py">ocr</a>(...) -> OcrResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detects every text region without translating. Reference: https://apinoa.com/docs/api-reference/image-translate/ocr
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.image_translate.ocr(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_language:** `OcrImageTranslateRequestSourceLanguage` — The text's language: ch, zh, zh-CN, zh-TW, chinese_cht, ja, japan, en, or auto.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — The image as raw bytes (not JSON, not base64). JPEG, PNG or WebP, up to 20 MB and 8192 × 8192 px.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.image_translate.<a href="src/apinoa/image_translate/client.py">supported_fonts</a>() -> SupportedFontsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reference: https://apinoa.com/docs/api-reference/image-translate/supported-fonts
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apinoa import Apinoa
from apinoa.environment import ApinoaEnvironment

client = Apinoa(
    api_key="<value>",
    environment=ApinoaEnvironment.DEFAULT,
)

client.image_translate.supported_fonts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

