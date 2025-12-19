# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:willGoToBackForwardListItem:inPageCache:)``

履歴項目への移動予定を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView willGoToBackForwardListItem:(WKBackForwardListItem *)item inPageCache:(BOOL)inPageCache WK_API_AVAILABLE(macos(10.13.4), ios(14.0));
```

## Discussion
shouldGoToBackForwardListItem で completionHandler 版が無い場合に、`willGoToBackForwardListItem` を呼ぶ。

## References
- [`WKNavigationDelegatePrivate.h#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L103)
- [`NavigationState.mm#L226`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L226)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
