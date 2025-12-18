# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:willPerformClientRedirectToURL:delay:)``

クライアントリダイレクト予定を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView willPerformClientRedirectToURL:(NSURL *)URL delay:(NSTimeInterval)delay;
```

## Discussion
willPerformClientRedirect で URL を NSURL に変換し、delay とともに呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L68)
- [`NavigationState.mm#L885`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L885)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
