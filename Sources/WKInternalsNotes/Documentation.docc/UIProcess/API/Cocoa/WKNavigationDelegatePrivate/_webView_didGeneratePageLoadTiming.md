# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:didGeneratePageLoadTiming:)``

ページロードタイミングを通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didGeneratePageLoadTiming:(_WKPageLoadTiming *)timing WK_API_AVAILABLE(macos(15.2), ios(18.2), visionos(2.2));
```

## Discussion
didGeneratePageLoadTiming で `WebPageLoadTiming` を `_WKPageLoadTiming` にラップして渡す。

## References
- [`WKNavigationDelegatePrivate.h#L105`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L105)
- [`NavigationState.mm#L230`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L230)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
