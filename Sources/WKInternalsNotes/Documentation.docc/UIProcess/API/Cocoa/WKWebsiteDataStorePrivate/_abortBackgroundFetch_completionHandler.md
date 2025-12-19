# ``WKInternalsNotes/WKWebsiteDataStore/_abortBackgroundFetch(_:completionHandler:)``

バックグラウンドフェッチを中断する。

## Objective-C Declaration
```objective-c
- (void)_abortBackgroundFetch:(NSString *)identifier completionHandler:(void(^_Nullable)(void))completionHandler WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
`completionHandler` が `nil` の場合は空のブロックに置き換える。`NetworkProcess` に abort を依頼し、完了後に `completionHandler` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L141)
- [`WKWebsiteDataStore.mm#L1386`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1386)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
