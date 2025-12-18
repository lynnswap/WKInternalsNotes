# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:renderingProgressDidChange:)``

レンダリング進捗の変化を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView renderingProgressDidChange:(_WKRenderingProgressEvents)progressEvents;
```

## Discussion
`LayoutMilestone` を `_WKRenderingProgressEvents` に変換して呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L75)
- [`NavigationState.mm#L1156`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L1156)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
