# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:requestNotificationPermissionForSecurityOrigin:decisionHandler:)``

通知許可を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView requestNotificationPermissionForSecurityOrigin:(WKSecurityOrigin *)securityOrigin decisionHandler:(void (^)(BOOL))decisionHandler WK_API_AVAILABLE(macos(10.13.4), ios(16.0));
```

## Discussion
UIDelegate::UIClient が `CompletionHandlerCallChecker` を使って securityOrigin を渡し、結果を completionHandler に返す。

## References
- [`WKUIDelegatePrivate.h#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L187)
- [`UIDelegate.mm#L224`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L224)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
