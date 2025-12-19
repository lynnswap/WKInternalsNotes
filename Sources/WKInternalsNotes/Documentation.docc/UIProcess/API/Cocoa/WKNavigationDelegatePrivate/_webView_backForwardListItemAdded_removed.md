# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:backForwardListItemAdded:removed:)``

履歴項目の追加/削除を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView backForwardListItemAdded:(WKBackForwardListItem *)itemAdded removed:(NSArray<WKBackForwardListItem *> *)itemsRemoved WK_API_AVAILABLE(macos(10.13.4), ios(18.4));
```

## Discussion
didChangeBackForwardList で追加 item と削除 items をラップし、配列にまとめて delegate へ渡す。

## References
- [`WKNavigationDelegatePrivate.h#L94`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L94)
- [`NavigationState.mm#L226`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L226)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
