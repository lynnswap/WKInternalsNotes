# ``WKInternalsNotes/WKWebsiteDataStore/_pauseBackgroundFetch(_:completionHandler:)``

バックグラウンドフェッチを一時停止する。

## Objective-C Declaration
```objective-c
-(void)_pauseBackgroundFetch:(NSString *)identifier completionHandler:(void(^_Nullable)(void))completionHandler WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
`completionHandler` が `nil` の場合は空のブロックに置き換え、`NetworkProcess` の `pauseBackgroundFetch` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L142`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L142)
- [`WKWebsiteDataStore.mm#L1395`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1395)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
