# ``WKInternalsNotes/WKWebsiteDataStore/_statisticsDatabaseHasAllTables(_:)``

統計データベースが全テーブルを持つか確認する。

## Objective-C Declaration
```objective-c
- (void)_statisticsDatabaseHasAllTables:(void (^)(BOOL))completionHandler WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`statisticsDatabaseHasAllTables` を呼び、結果を `completionHandler` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L92`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L92)
- [`WKWebsiteDataStore.mm#L1077`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1077)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
