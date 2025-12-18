# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:didNegotiateModernTLSForURL:)``

Modern TLS をネゴシエートした URL を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didNegotiateModernTLSForURL:(NSURL *)url WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
didNegotiateModernTLS で URL を NSURL に変換して呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L85)
- [`NavigationState.mm#L1236`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L1236)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
