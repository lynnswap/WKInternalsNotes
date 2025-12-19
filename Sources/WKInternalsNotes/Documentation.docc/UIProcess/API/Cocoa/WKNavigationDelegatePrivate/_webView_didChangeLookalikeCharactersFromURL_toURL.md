# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:didChangeLookalikeCharactersFromURL:toURL:)``

見間違い文字の補正後 URL を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didChangeLookalikeCharactersFromURL:(NSURL *)originalURL toURL:(NSURL *)adjustedURL WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Discussion
didApplyLinkDecorationFiltering で original/adjusted URL を NSURL に変換して呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L87)
- [`NavigationState.mm#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
