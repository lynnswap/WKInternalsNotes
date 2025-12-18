# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:navigation:didSameDocumentNavigation:)``

same-document ナビゲーションを通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView navigation:(WKNavigation *)navigation didSameDocumentNavigation:(_WKSameDocumentNavigationType)navigationType;
```

## Discussion
didSameDocumentNavigation で WKNavigation と `_WKSameDocumentNavigationType` を変換して渡す。

## References
- [`WKNavigationDelegatePrivate.h#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L73)
- [`NavigationState.mm#L1140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L1140)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
