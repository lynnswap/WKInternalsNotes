# ``WKInternalsNotes/WKWebsiteDataStore/_getResourceLoadStatisticsDataSummary(_:)``

リソースロード統計のサマリを取得する。

## Objective-C Declaration
```objective-c
- (void)_getResourceLoadStatisticsDataSummary:(void (^)(NSArray<_WKResourceLoadStatisticsThirdParty *> *))completionHandler WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
`getResourceLoadStatisticsDataSummary` の結果を `_WKResourceLoadStatisticsThirdParty` 配列に変換して返す。

## References
- [`WKWebsiteDataStorePrivate.h#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L85)
- [`WKWebsiteDataStore.mm#L1049`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1049)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
