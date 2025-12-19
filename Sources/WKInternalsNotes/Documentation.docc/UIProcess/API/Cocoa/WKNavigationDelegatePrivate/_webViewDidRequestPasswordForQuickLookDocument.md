# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webViewDidRequestPasswordForQuickLookDocument(_:)``

Quick Look ドキュメントのパスワード要求開始を通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewDidRequestPasswordForQuickLookDocument:(WKWebView *)webView WK_API_AVAILABLE(ios(11.0));
```

## Discussion
`PLATFORM(IOS_FAMILY)` のみで、didRequestPasswordForQuickLookDocument から呼び出される。

## References
- [`WKNavigationDelegatePrivate.h#L118`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L118)
- [`NavigationState.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
