# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewDidRequestPointerLock(_:completionHandler:)``

ポインターロック要求を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webViewDidRequestPointerLock:(WKWebView *)webView completionHandler:(void (^)(BOOL))completionHandler WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
UIDelegate::UIClient が `CompletionHandlerCallChecker` を使って許可可否を delegate に問い合わせる。

## References
- [`WKUIDelegatePrivate.h#L155`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L155)
- [`UIDelegate.mm#L209`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L209)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
