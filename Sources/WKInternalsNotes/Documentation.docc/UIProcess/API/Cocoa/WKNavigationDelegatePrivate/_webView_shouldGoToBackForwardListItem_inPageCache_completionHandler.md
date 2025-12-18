# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:shouldGoToBackForwardListItem:inPageCache:completionHandler:)``

履歴項目へ移動するかどうかを問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView shouldGoToBackForwardListItem:(WKBackForwardListItem *)item inPageCache:(BOOL)inPageCache completionHandler:(void (^)(BOOL shouldGoToItem))completionHandler WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
shouldGoToBackForwardListItem で completionHandler を渡して呼び出し、未実装の場合は willGoToBackForwardListItem の通知後に true で継続する。

## References
- [`WKNavigationDelegatePrivate.h#L131`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L131)
- [`NavigationState.mm#L421`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L421)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
