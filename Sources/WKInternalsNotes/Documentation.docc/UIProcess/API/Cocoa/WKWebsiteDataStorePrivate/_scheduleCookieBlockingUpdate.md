# ``WKInternalsNotes/WKWebsiteDataStore/_scheduleCookieBlockingUpdate(_:)``

Cookie ブロック更新をスケジュールする。

## Objective-C Declaration
```objective-c
- (void)_scheduleCookieBlockingUpdate:(void (^)(void))completionHandler WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
`scheduleCookieBlockingUpdate` を呼び、完了後に `completionHandler` を実行する。

## References
- [`WKWebsiteDataStorePrivate.h#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L81)
- [`WKWebsiteDataStore.mm#L1000`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1000)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
