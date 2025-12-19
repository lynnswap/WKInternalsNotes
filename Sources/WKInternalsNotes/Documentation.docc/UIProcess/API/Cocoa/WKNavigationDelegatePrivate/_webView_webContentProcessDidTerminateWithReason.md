# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:webContentProcessDidTerminateWithReason:)``

Web コンテンツプロセスの終了理由を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView webContentProcessDidTerminateWithReason:(_WKProcessTerminationReason)reason WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
processDidTerminate で `ProcessTerminationReason` を `_WKProcessTerminationReason` に変換し、理由付き delegate があればそちらを呼ぶ。

## References
- [`WKNavigationDelegatePrivate.h#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L84)
- [`NavigationState.mm#L194`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L194)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
