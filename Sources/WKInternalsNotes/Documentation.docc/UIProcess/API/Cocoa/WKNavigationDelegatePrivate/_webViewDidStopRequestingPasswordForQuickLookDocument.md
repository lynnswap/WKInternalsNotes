# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webViewDidStopRequestingPasswordForQuickLookDocument(_:)``

Quick Look ドキュメントのパスワード要求停止を通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewDidStopRequestingPasswordForQuickLookDocument:(WKWebView *)webView WK_API_AVAILABLE(ios(17.0));
```

## Discussion
`PLATFORM(IOS_FAMILY)` のみで、didStopRequestingPasswordForQuickLookDocument から呼び出される。

## References
- [`WKNavigationDelegatePrivate.h#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L119)
- [`NavigationState.mm#L351`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L351)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
