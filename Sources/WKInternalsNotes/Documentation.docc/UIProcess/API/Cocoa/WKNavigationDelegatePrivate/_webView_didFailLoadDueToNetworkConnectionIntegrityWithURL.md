# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:didFailLoadDueToNetworkConnectionIntegrityWithURL:)``

ネットワーク接続整合性の問題による失敗を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didFailLoadDueToNetworkConnectionIntegrityWithURL:(NSURL *)url WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Discussion
didBlockLoadToKnownTracker で URL を NSURL に変換して呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L109)
- [`NavigationState.mm#L1061`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L1061)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
