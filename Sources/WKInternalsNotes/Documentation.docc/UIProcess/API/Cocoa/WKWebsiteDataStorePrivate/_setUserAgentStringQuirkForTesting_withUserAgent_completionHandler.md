# ``WKInternalsNotes/WKWebsiteDataStore/_setUserAgentStringQuirkForTesting(_:withUserAgent:completionHandler:)``

テスト用に User Agent 文字列の quirk を設定する。

## Objective-C Declaration
```objective-c
- (void)_setUserAgentStringQuirkForTesting:(NSString *)domain withUserAgent:(NSString *)userAgent completionHandler:(void (^)(void))completionHandler WK_API_AVAILABLE(macos(14.4), ios(17.4), visionos(1.1));
```

## Discussion
`setUserAgentStringQuirkForTesting` を呼び、完了後に `completionHandler` を実行する。

## References
- [`WKWebsiteDataStorePrivate.h#L107`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L107)
- [`WKWebsiteDataStore.mm#L1122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1122)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
