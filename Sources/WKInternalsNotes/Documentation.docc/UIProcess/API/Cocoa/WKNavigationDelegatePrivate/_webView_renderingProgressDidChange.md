# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:renderingProgressDidChange:)``

レンダリング進捗の変化を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView renderingProgressDidChange:(_WKRenderingProgressEvents)progressEvents;
```

## Discussion
`LayoutMilestone` を `_WKRenderingProgressEvents` に変換して呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L66)
- [`NavigationState.mm#L191`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L191)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
