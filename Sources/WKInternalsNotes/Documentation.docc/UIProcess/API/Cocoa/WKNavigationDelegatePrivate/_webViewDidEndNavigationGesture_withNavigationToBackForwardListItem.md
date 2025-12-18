# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webViewDidEndNavigationGesture(_:withNavigationToBackForwardListItem:)``

ナビゲーションジェスチャ終了を通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewDidEndNavigationGesture:(WKWebView *)webView withNavigationToBackForwardListItem:(WKBackForwardListItem *)item;
```

## Discussion
navigationGestureDidEnd で `willNavigate` に応じた item を渡して呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L91)
- [`NavigationState.mm#L302`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L302)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
