# ``WKInternalsNotes/WKWebsiteDataStore/_logUserInteraction(_:completionHandler:)``

ユーザー操作を記録する。

## Objective-C Declaration
```objective-c
- (void)_logUserInteraction:(NSURL *)domain completionHandler:(void (^)(void))completionHandler WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
`logUserInteraction` を呼び、完了後に `completionHandler` を実行する。

## References
- [`WKWebsiteDataStorePrivate.h#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L82)
- [`WKWebsiteDataStore.mm#L1007`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1007)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
