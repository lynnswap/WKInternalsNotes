# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:didPerformClientRedirectFromURL:toURL:)``

クライアントリダイレクト完了を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didPerformClientRedirectFromURL:(NSURL *)sourceURL toURL:(NSURL *)destinationURL;
```

## Discussion
didPerformClientRedirect で source/destination URL を NSURL に変換して呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L69)
- [`NavigationState.mm#L904`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L904)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
