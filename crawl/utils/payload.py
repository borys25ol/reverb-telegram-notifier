"""
Module with GraphQL request payloads.
"""


def build_product_payload(
    slug: str,
    limit: int,
    item_region: str | None = None,
    price_min: str | None = None,
    price_max: str | None = None,
    ships_to: str | None = None,
) -> dict:
    return {
        "operationName": "Csp_Filters_And_ListingsQuery",
        "variables": {
            "aggs": ["CATEGORY_SLUGS", "CONDITION_SLUGS", "DECADES", "TRAITS"],
            "bumpLimit": 3,
            "canonicalFinishes": [],
            "conditionSlugs": [],
            "cspSlug": slug,
            "fallbackToEverywhereElse": False,
            "fretboardMaterial": None,
            "includeFullFinancingFields": True,
            "itemRegion": item_region or "US",
            "limit": limit,
            "offset": 0,
            "priceMin": price_min,
            "priceMax": price_max,
            "shippingRegionCode": ships_to,
            "shippingRegionCodes": [ships_to] if ships_to else [],
            "shouldHideBump": True,
            "shouldSkipTracking": False,
            "showBestPriceListingsSort": False,
            "showLikelihoodToSellSort": False,
            "sort": "NONE",
            "traitValues": [],
            "withProximityFilter": {"proximity": False},
        },
        "query": 'query Csp_Filters_And_ListingsQuery($acceptsAffirm: Boolean, $acceptsGiftCards: Boolean, $acceptsOffers: Boolean, $acceptsPaymentPlans: Boolean, $aggs: [reverb_search_ListingsSearchRequest_Aggregation], $bumpLimit: Int, $dealsAndSteals: Boolean, $decades: [String], $canonicalFinishes: [String], $categorySlugs: [String], $combinedShipping: Boolean, $conditionSlugs: [String], $cspSlug: String, $excludeLocalPickupOnly: Boolean, $fallbackToEverywhereElse: Boolean, $freeExpeditedShipping: Boolean, $freeShipping: Boolean, $fretboardMaterial: String, $includeFullFinancingFields: Boolean!, $itemRegion: String, $itemRegionRelation: reverb_search_ListingItemRegionRelation, $limit: Int, $localPickup: Boolean, $offset: Int, $onSale: Boolean, $preferredSeller: Boolean, $priceMin: String, $priceMax: String, $query: String, $shippingRegionCode: String, $shippingRegionCodes: [String], $shouldHideBump: Boolean!, $shouldSkipTracking: Boolean!, $showBestPriceListingsSort: Boolean, $showLikelihoodToSellSort: Boolean, $sort: reverb_search_ListingsSearchRequest_Sort, $sortSlug: String, $traitValues: [String], $withProximityFilter: Input_reverb_search_ProximityFilterRequest, $yearMax: String, $yearMin: String) {\n  allListings: listingsSearch(input: {cspSlug: $cspSlug, conditionSlugs: $conditionSlugs, statuses: ["live"], canonicalFinishes: $canonicalFinishes, traitValues: $traitValues, withAggregations: $aggs, priceMin: $priceMin, priceMax: $priceMax, query: $query, categorySlugs: $categorySlugs, sort: $sort, sortSlug: $sortSlug, localPickup: $localPickup, acceptsOffers: $acceptsOffers, onSale: $onSale, excludeLocalPickupOnly: $excludeLocalPickupOnly, freeShipping: $freeShipping, freeExpeditedShipping: $freeExpeditedShipping, combinedShipping: $combinedShipping, acceptsPaymentPlans: $acceptsPaymentPlans, dealsAndSteals: $dealsAndSteals, decades: $decades, yearMax: $yearMax, yearMin: $yearMin, acceptsGiftCards: $acceptsGiftCards, preferredSeller: $preferredSeller, acceptsAffirm: $acceptsAffirm, itemRegion: $itemRegion, itemRegionRelation: $itemRegionRelation, shippingRegionCodes: $shippingRegionCodes, withProximityFilter: $withProximityFilter, fallbackToEverywhereElse: $fallbackToEverywhereElse, showBestPriceListingsSort: $showBestPriceListingsSort, showLikelihoodToSellSort: $showLikelihoodToSellSort, offset: $offset, limit: $limit}) {\n    total\n    offset\n    filters {\n      ...NestedFilter\n      __typename\n    }\n    listings {\n      _id\n      ...ListingData\n      ...ListingsCollection\n      ...mParticleListingFields @skip(if: $shouldSkipTracking)\n      ...FullFinancingFields @include(if: $includeFullFinancingFields)\n      ...ListingGreatValueData\n      __typename\n    }\n    fallbackListings {\n      _id\n      ...ListingData\n      ...ListingsCollection\n      ...mParticleListingFields @skip(if: $shouldSkipTracking)\n      ...FullFinancingFields @include(if: $includeFullFinancingFields)\n      ...ListingGreatValueData\n      __typename\n    }\n    __typename\n  }\n  allBumped: bumpedSortedListings(input: {cspSlug: $cspSlug, conditionSlugs: $conditionSlugs, statuses: ["live"], sort: PRICE_ASC, filterSuperRegionCode: $shippingRegionCode, bumpedOnly: true, canonicalFinishes: $canonicalFinishes, traitValues: $traitValues, withAggregations: $aggs, priceMin: $priceMin, priceMax: $priceMax, query: $query, categorySlugs: $categorySlugs, localPickup: $localPickup, acceptsOffers: $acceptsOffers, onSale: $onSale, freeShipping: $freeShipping, freeExpeditedShipping: $freeExpeditedShipping, combinedShipping: $combinedShipping, acceptsPaymentPlans: $acceptsPaymentPlans, dealsAndSteals: $dealsAndSteals, decades: $decades, yearMax: $yearMax, yearMin: $yearMin, acceptsGiftCards: $acceptsGiftCards, preferredSeller: $preferredSeller, acceptsAffirm: $acceptsAffirm, shippingRegionCodes: $shippingRegionCodes, withProximityFilter: $withProximityFilter, bumpedSortedListingsQuery: {condition: "all", bumpedMax: $bumpLimit, total: $bumpLimit, itemRegion: $itemRegion}}) @skip(if: $shouldHideBump) {\n    listings {\n      _id\n      ...ListingData\n      ...ListingsCollection\n      ...mParticleListingFields @skip(if: $shouldSkipTracking)\n      ...FullFinancingFields @include(if: $includeFullFinancingFields)\n      ...BumpKey\n      __typename\n    }\n    __typename\n  }\n  finishAgg: listingsAggregationSearch(input: {withAggregations: CANONICAL_FINISH, cspSlug: $cspSlug}) {\n    aggregationResults {\n      name\n      aggregationDetails {\n        key\n        count\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  fretboardMaterialAgg: listingsAggregationSearch(input: {canonicalFinishes: $canonicalFinishes, withAggregations: TRAITS, cspSlug: $cspSlug, traitValues: [$fretboardMaterial]}) {\n    aggregationResults {\n      name\n      displayName\n      aggregationDetails {\n        key\n        displayName\n        count\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ListingsCollection on Listing {\n  _id\n  id\n  bumped\n  categoryUuids\n  slug\n  title\n  description\n  listingType\n  condition {\n    displayName\n    conditionSlug\n    __typename\n  }\n  price {\n    amountCents\n    display\n    __typename\n  }\n  pricing {\n    buyerPrice {\n      display\n      currency\n      amountCents\n      __typename\n    }\n    originalPrice {\n      display\n      __typename\n    }\n    ribbon {\n      display\n      __typename\n    }\n    __typename\n  }\n  images(input: {transform: "card_square", count: 3, scope: "photos", type: "Product"}) {\n    source\n    __typename\n  }\n  watching\n  state\n  stateDescription\n  shipping {\n    shippingPrices {\n      shippingMethod\n      carrierCalculated\n      destinationPostalCodeNeeded\n      rate {\n        amount\n        amountCents\n        currency\n        display\n        __typename\n      }\n      __typename\n    }\n    freeExpeditedShipping\n    localPickupOnly\n    __typename\n  }\n  shop {\n    _id\n    address {\n      country {\n        countryCode\n        name\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  ...AddToCartButtonData\n  ...WatchBadgeData\n  ...ListingGreatValueData\n  ...ListingCreateOfferButtonData\n  __typename\n}\n\nfragment WatchBadgeData on Listing {\n  _id\n  id\n  title\n  watching\n  watchThumbnails: images(input: {type: "Product", scope: "photos", transform: "card_square", count: 1}) {\n    source\n    __typename\n  }\n  __typename\n}\n\nfragment AddToCartButtonData on Listing {\n  _id\n  id\n  sellerId\n  preorderInfo {\n    onPreorder\n    estimatedShipDate {\n      seconds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ListingGreatValueData on Listing {\n  _id\n  pricing {\n    buyerPrice {\n      currency\n      amountCents\n      __typename\n    }\n    __typename\n  }\n  condition {\n    conditionSlug\n    __typename\n  }\n  priceRecommendation {\n    priceMiddle {\n      amountCents\n      currency\n      __typename\n    }\n    __typename\n  }\n  shop {\n    _id\n    address {\n      country {\n        countryCode\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  currency\n  __typename\n}\n\nfragment ListingCreateOfferButtonData on Listing {\n  id\n  _id\n  state\n  listingType\n  ...mParticleListingFields\n  __typename\n}\n\nfragment mParticleListingFields on Listing {\n  id\n  _id\n  title\n  brandSlug\n  categoryRootUuid\n  make\n  categoryUuids\n  state\n  listingType\n  bumpEligible\n  shopId\n  inventory\n  soldAsIs\n  acceptedPaymentMethods\n  currency\n  condition {\n    conditionUuid\n    conditionSlug\n    __typename\n  }\n  categories {\n    _id\n    slug\n    rootSlug\n    __typename\n  }\n  csp {\n    _id\n    id\n    slug\n    brand {\n      _id\n      slug\n      __typename\n    }\n    __typename\n  }\n  pricing {\n    buyerPrice {\n      amount\n      currency\n      amountCents\n      __typename\n    }\n    __typename\n  }\n  publishedAt {\n    seconds\n    __typename\n  }\n  sale {\n    code\n    buyerIneligibilityReason\n    __typename\n  }\n  shipping {\n    shippingPrices {\n      shippingMethod\n      carrierCalculated\n      destinationPostalCodeNeeded\n      rate {\n        amount\n        amountCents\n        currency\n        display\n        __typename\n      }\n      __typename\n    }\n    freeExpeditedShipping\n    localPickupOnly\n    localPickup\n    __typename\n  }\n  shop {\n    _id\n    address {\n      countryCode\n      __typename\n    }\n    returnPolicy {\n      newReturnWindowDays\n      usedReturnWindowDays\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ListingData on Listing {\n  _id\n  upc\n  finish\n  model\n  shopUuid\n  ...SellerInfoData\n  __typename\n}\n\nfragment SellerInfoData on Listing {\n  _id\n  seller {\n    _id\n    feedbackSummary {\n      receivedCount\n      rollingRatingPercentage\n      __typename\n    }\n    __typename\n  }\n  shop {\n    _id\n    name\n    slug\n    preferredSeller\n    quickShipper\n    quickResponder\n    address {\n      displayLocation\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment NestedFilter on reverb_search_Filter {\n  name\n  key\n  aggregationName\n  widgetType\n  options {\n    count {\n      value\n      __typename\n    }\n    name\n    selected\n    autoselected\n    paramName\n    setValues\n    unsetValues\n    all\n    optionValue\n    trackingValue\n    subFilter {\n      widgetType\n      options {\n        count {\n          value\n          __typename\n        }\n        name\n        selected\n        autoselected\n        paramName\n        setValues\n        unsetValues\n        all\n        optionValue\n        trackingValue\n        subFilter {\n          widgetType\n          options {\n            count {\n              value\n              __typename\n            }\n            name\n            selected\n            autoselected\n            paramName\n            setValues\n            unsetValues\n            all\n            optionValue\n            trackingValue\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment FullFinancingFields on Listing {\n  _id\n  estimatedMonthlyPaymentPlan {\n    estimatedMonthlyPayment {\n      display\n      __typename\n    }\n    maxTermMonth\n    availableTermMonths\n    lowestAprAtMaxTerm\n    zeroPercentFinancingPlan\n    splitPay\n    __typename\n  }\n  pricing {\n    buyerPrice {\n      display\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment BumpKey on Listing {\n  _id\n  bumpKey {\n    key\n    __typename\n  }\n  __typename\n}\n',
    }


def build_search_payload(
    query: str,
    limit: int,
    product_type: str | None = None,
    category: str | None = None,
    make: str | None = None,
    condition: str | None = None,
    price_min: str | None = None,
    price_max: str | None = None,
    ships_to: str | None = None,
) -> dict:
    category_slugs = [slug for slug in (product_type, category) if slug]
    return {
        "operationName": "Core_Marketplace_CombinedMarketplaceSearch",
        "variables": {
            "inputListings": {
                "query": query,
                "priceMin": price_min,
                "priceMax": price_max,
                "categorySlugs": category_slugs,
                "brandSlugs": [make] if make else [],
                "conditionSlugs": [condition] if condition else [],
                "shippingRegionCodes": [ships_to] if ships_to else [],
                "itemState": [],
                "itemCity": [],
                "curatedSetSlugs": [],
                "saleSlugs": [],
                "withProximityFilter": {"proximity": False},
                "boostedItemRegionCode": "US",
                "useExperimentalRecall": True,
                "traitValues": [],
                "excludeCategoryUuids": [],
                "excludeBrandSlugs": [],
                "likelihoodToSellExperimentGroup": 3,
                "countryOfOrigin": [],
                "contexts": [],
                "autodirects": "IMPROVED_DATA",
                "multiClientExperiments": [
                    {"name": "ltr_v3_marketplace_2024_06", "group": "1"},
                    {"name": "ltr_v4_marketplace_2024_07", "group": "0"},
                ],
                "canonicalFinishes": [],
                "limit": limit,
                "offset": 0,
                "fallbackToOr": True,
                "sort": "NONE",
            },
            "inputBumped": {
                "query": query,
                "priceMin": price_min,
                "priceMax": price_max,
                "categorySlugs": category_slugs,
                "brandSlugs": [make] if make else [],
                "conditionSlugs": [condition] if condition else [],
                "shippingRegionCodes": [ships_to] if ships_to else [],
                "itemState": [],
                "itemCity": [],
                "curatedSetSlugs": [],
                "saleSlugs": [],
                "withProximityFilter": {"proximity": False},
                "boostedItemRegionCode": "US",
                "useExperimentalRecall": True,
                "traitValues": [],
                "excludeCategoryUuids": [],
                "excludeBrandSlugs": [],
                "likelihoodToSellExperimentGroup": 3,
                "countryOfOrigin": [],
                "contexts": [],
                "autodirects": "IMPROVED_DATA",
                "multiClientExperiments": [
                    {"name": "ltr_v3_marketplace_2024_06", "group": "1"},
                    {"name": "ltr_v4_marketplace_2024_07", "group": "0"},
                ],
                "canonicalFinishes": [],
                "limit": limit,
                "offset": 0,
                "boostByBumpRate": True,
                "bumpedOnly": True,
                "sort": "NONE",
            },
            "inputAggs": {
                "query": query,
                "priceMin": price_min,
                "priceMax": price_max,
                "categorySlugs": category_slugs,
                "brandSlugs": [make] if make else [],
                "conditionSlugs": [condition] if condition else [],
                "shippingRegionCodes": [ships_to] if ships_to else [],
                "itemState": [],
                "itemCity": [],
                "curatedSetSlugs": [],
                "saleSlugs": [],
                "withProximityFilter": {"proximity": False},
                "boostedItemRegionCode": "US",
                "useExperimentalRecall": True,
                "traitValues": [],
                "excludeCategoryUuids": [],
                "excludeBrandSlugs": [],
                "likelihoodToSellExperimentGroup": 3,
                "countryOfOrigin": [],
                "contexts": [],
                "autodirects": "IMPROVED_DATA",
                "multiClientExperiments": [
                    {"name": "ltr_v3_marketplace_2024_06", "group": "1"},
                    {"name": "ltr_v4_marketplace_2024_07", "group": "0"},
                ],
                "canonicalFinishes": [],
                "limit": 0,
                "withAggregations": [
                    "CATEGORY_SLUGS",
                    "BRAND_SLUGS",
                    "CONDITION_SLUGS",
                    "DECADES",
                    "CURATED_SETS",
                    "COUNTRY_OF_ORIGIN",
                ],
                "fallbackToOr": True,
            },
            "shouldntLoadBumps": False,
            "shouldntLoadSuggestions": False,
            "usingListView": True,
            "signalGroups": ["MP_LIST_CARD"],
            "useSignalSystem": False,
        },
        "query": 'query Core_Marketplace_CombinedMarketplaceSearch($inputListings: Input_reverb_search_ListingsSearchRequest, $inputBumped: Input_reverb_search_ListingsSearchRequest, $inputAggs: Input_reverb_search_ListingsSearchRequest, $shouldntLoadBumps: Boolean!, $shouldntLoadSuggestions: Boolean!, $usingListView: Boolean!, $signalGroups: [reverb_signals_Signal_Group], $useSignalSystem: Boolean!) {\n  bumpedSearch: listingsSearch(input: $inputBumped) @skip(if: $shouldntLoadBumps) {\n    listings {\n      _id\n      ...ListingCardFields\n      ...WatchBadgeData\n      ...BumpKey\n      ...ShopFields\n      ...ListViewListings @include(if: $usingListView)\n      signals(input: {groups: $signalGroups}) @include(if: $useSignalSystem) {\n        ...ListingCardSignalsData\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  aggsSearch: listingsSearch(input: $inputAggs) {\n    filters {\n      ...NestedFilter\n      __typename\n    }\n    __typename\n  }\n  listingsSearch(input: $inputListings) {\n    total\n    offset\n    limit\n    suggestedQueries\n    eligibleAutodirects\n    listings {\n      _id\n      esScore\n      ...ListingCardFields\n      ...WatchBadgeData\n      ...InOtherCartsCardData @skip(if: $useSignalSystem)\n      ...ShopFields\n      ...ListViewListings @include(if: $usingListView)\n      signals(input: {groups: $signalGroups}) @include(if: $useSignalSystem) {\n        ...ListingCardSignalsData\n        __typename\n      }\n      __typename\n    }\n    fallbackListings {\n      _id\n      ...ListingCardFields\n      ...InOtherCartsCardData @skip(if: $useSignalSystem)\n      ...WatchBadgeData\n      signals(input: {groups: $signalGroups}) @include(if: $useSignalSystem) {\n        ...ListingCardSignalsData\n        __typename\n      }\n      __typename\n    }\n    suggestions @skip(if: $shouldntLoadSuggestions) {\n      ...MarketplaceSuggestions\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ListingCardFields on Listing {\n  _id\n  ...ListingForBuyerFields\n  ...WatchBadgeData\n  ...ListingCreateOfferButtonData\n  __typename\n}\n\nfragment ListingForBuyerFields on Listing {\n  _id\n  id\n  title\n  slug\n  listingType\n  make\n  model\n  upc\n  state\n  stateDescription\n  bumped\n  watching\n  soldAsIs\n  usOutlet\n  publishedAt {\n    seconds\n    __typename\n  }\n  condition {\n    displayName\n    conditionSlug\n    conditionUuid\n    __typename\n  }\n  pricing {\n    buyerPrice {\n      display\n      currency\n      amount\n      amountCents\n      __typename\n    }\n    originalPrice {\n      display\n      __typename\n    }\n    ribbon {\n      display\n      reason\n      __typename\n    }\n    typicalNewPriceDisplay {\n      amountDisplay\n      descriptionDisplay\n      savingsDisplay\n      __typename\n    }\n    originalPriceDescription\n    __typename\n  }\n  images(\n    input: {transform: "card_square", count: 3, scope: "photos", type: "Product"}\n  ) {\n    source\n    __typename\n  }\n  shipping {\n    shippingPrices {\n      _id\n      shippingMethod\n      carrierCalculated\n      destinationPostalCodeNeeded\n      rate {\n        amount\n        amountCents\n        currency\n        display\n        __typename\n      }\n      __typename\n    }\n    freeExpeditedShipping\n    localPickupOnly\n    localPickup\n    __typename\n  }\n  shop {\n    _id\n    name\n    returnPolicy {\n      usedReturnWindowDays\n      newReturnWindowDays\n      __typename\n    }\n    address {\n      _id\n      locality\n      region\n      country {\n        _id\n        countryCode\n        name\n        __typename\n      }\n      displayLocation\n      __typename\n    }\n    __typename\n  }\n  ...ListingForBuyerShippingFields\n  ...ListingGreatValueData\n  __typename\n}\n\nfragment ListingGreatValueData on Listing {\n  _id\n  pricing {\n    buyerPrice {\n      currency\n      amountCents\n      __typename\n    }\n    __typename\n  }\n  condition {\n    conditionSlug\n    __typename\n  }\n  priceRecommendation {\n    priceMiddle {\n      amountCents\n      currency\n      __typename\n    }\n    __typename\n  }\n  shop {\n    _id\n    address {\n      _id\n      country {\n        _id\n        countryCode\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  currency\n  __typename\n}\n\nfragment ListingForBuyerShippingFields on Listing {\n  _id\n  shipping {\n    freeExpeditedShipping\n    localPickupOnly\n    shippingPrices {\n      _id\n      shippingMethod\n      carrierCalculated\n      regional\n      destinationPostalCodeNeeded\n      rate {\n        amount\n        amountCents\n        currency\n        display\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ListingCreateOfferButtonData on Listing {\n  id\n  _id\n  state\n  listingType\n  sellerId\n  isBuyerOfferEligible\n  ...mParticleListingFields\n  __typename\n}\n\nfragment mParticleListingFields on Listing {\n  id\n  _id\n  title\n  brandSlug\n  categoryRootUuid\n  make\n  categoryUuids\n  state\n  listingType\n  bumpEligible\n  shopId\n  inventory\n  soldAsIs\n  acceptedPaymentMethods\n  currency\n  usOutlet\n  condition {\n    conditionUuid\n    conditionSlug\n    __typename\n  }\n  categories {\n    _id\n    slug\n    rootSlug\n    __typename\n  }\n  csp {\n    _id\n    id\n    slug\n    brand {\n      _id\n      slug\n      __typename\n    }\n    __typename\n  }\n  pricing {\n    buyerPrice {\n      amount\n      currency\n      amountCents\n      __typename\n    }\n    __typename\n  }\n  publishedAt {\n    seconds\n    __typename\n  }\n  sale {\n    id\n    code\n    buyerIneligibilityReason\n    __typename\n  }\n  shipping {\n    shippingPrices {\n      _id\n      shippingMethod\n      carrierCalculated\n      destinationPostalCodeNeeded\n      rate {\n        amount\n        amountCents\n        currency\n        display\n        __typename\n      }\n      __typename\n    }\n    freeExpeditedShipping\n    localPickupOnly\n    localPickup\n    __typename\n  }\n  shop {\n    _id\n    address {\n      _id\n      countryCode\n      __typename\n    }\n    returnPolicy {\n      newReturnWindowDays\n      usedReturnWindowDays\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment WatchBadgeData on Listing {\n  _id\n  id\n  title\n  sellerId\n  watching\n  watchThumbnails: images(\n    input: {type: "Product", scope: "photos", transform: "card_square", count: 1}\n  ) {\n    source\n    __typename\n  }\n  __typename\n}\n\nfragment BumpKey on Listing {\n  _id\n  bumpKey {\n    key\n    __typename\n  }\n  __typename\n}\n\nfragment ShopFields on Listing {\n  _id\n  shop {\n    _id\n    address {\n      _id\n      locality\n      countryCode\n      region\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment InOtherCartsCardData on Listing {\n  _id\n  id\n  otherBuyersWithListingInCartCounts\n  __typename\n}\n\nfragment NestedFilter on reverb_search_Filter {\n  name\n  key\n  aggregationName\n  widgetType\n  options {\n    count {\n      value\n      __typename\n    }\n    name\n    selected\n    autoselected\n    paramName\n    setValues\n    unsetValues\n    all\n    optionValue\n    trackingValue\n    subFilter {\n      widgetType\n      options {\n        count {\n          value\n          __typename\n        }\n        name\n        selected\n        autoselected\n        paramName\n        setValues\n        unsetValues\n        all\n        optionValue\n        trackingValue\n        subFilter {\n          widgetType\n          options {\n            count {\n              value\n              __typename\n            }\n            name\n            selected\n            autoselected\n            paramName\n            setValues\n            unsetValues\n            all\n            optionValue\n            trackingValue\n            subFilter {\n              widgetType\n              options {\n                count {\n                  value\n                  __typename\n                }\n                name\n                selected\n                autoselected\n                paramName\n                setValues\n                unsetValues\n                all\n                optionValue\n                trackingValue\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment MarketplaceSuggestions on reverb_search_SearchResponse_Suggestion {\n  text\n  __typename\n}\n\nfragment ListViewListings on Listing {\n  _id\n  id\n  categoryUuids\n  state\n  shop {\n    _id\n    name\n    slug\n    preferredSeller\n    quickShipper\n    quickResponder\n    address {\n      _id\n      locality\n      region\n      displayLocation\n      country {\n        _id\n        countryCode\n        name\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  seller {\n    _id\n    feedbackSummary {\n      receivedCount\n      rollingRatingPercentage\n      __typename\n    }\n    __typename\n  }\n  csp {\n    _id\n    webLink {\n      href\n      __typename\n    }\n    __typename\n  }\n  ...AddToCartButtonFields\n  ...ListingCardFields\n  ...ListingCreateOfferButtonData\n  ...InOtherCartsCardData\n  __typename\n}\n\nfragment AddToCartButtonFields on Listing {\n  _id\n  id\n  sellerId\n  listingType\n  pricing {\n    buyerPrice {\n      amount\n      amountCents\n      __typename\n    }\n    __typename\n  }\n  preorderInfo {\n    onPreorder\n    estimatedShipDate {\n      seconds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ListingCardSignalsData on reverb_signals_Signal {\n  name\n  title\n  icon\n  __typename\n}\n',
    }
