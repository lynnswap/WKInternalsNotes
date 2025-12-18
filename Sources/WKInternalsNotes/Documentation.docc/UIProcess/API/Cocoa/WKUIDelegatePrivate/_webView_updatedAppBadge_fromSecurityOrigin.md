# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:updatedAppBadge:fromSecurityOrigin:)``

アプリバッジ更新を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView updatedAppBadge:(NSNumber *)badge fromSecurityOrigin:(WKSecurityOrigin *)origin WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Discussion
UIDelegate::UIClient が `NSNumber` の badge 値と `WKSecurityOrigin` を渡して更新を通知する。

## References
- [`WKUIDelegatePrivate.h#L217`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L217)
- [`UIDelegate.mm#L2017`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L2017)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
