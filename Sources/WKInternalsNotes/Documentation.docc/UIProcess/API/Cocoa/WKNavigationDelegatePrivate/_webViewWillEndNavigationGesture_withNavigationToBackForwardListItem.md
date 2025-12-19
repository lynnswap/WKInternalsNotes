# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webViewWillEndNavigationGesture(_:withNavigationToBackForwardListItem:)``

ナビゲーションジェスチャ終了予定を通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewWillEndNavigationGesture:(WKWebView *)webView withNavigationToBackForwardListItem:(WKBackForwardListItem *)item;
```

## Discussion
navigationGestureWillEnd で `willNavigate` に応じた item を渡して呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L93`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L93)
- [`NavigationState.mm#L228`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L228)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
