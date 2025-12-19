# ``WKInternalsNotes/WKWebsiteDataStore/_resumeBackgroundFetch(_:completionHandler:)``

バックグラウンドフェッチを再開する。

## Objective-C Declaration
```objective-c
-(void)_resumeBackgroundFetch:(NSString *)identifier completionHandler:(void(^_Nullable)(void))completionHandler WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
`completionHandler` が `nil` の場合は空のブロックに置き換え、`NetworkProcess` の `resumeBackgroundFetch` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L143`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L143)
- [`WKWebsiteDataStore.mm#L1405`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1405)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
