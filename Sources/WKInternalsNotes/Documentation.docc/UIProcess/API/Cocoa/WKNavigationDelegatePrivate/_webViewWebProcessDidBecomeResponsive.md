# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webViewWebProcessDidBecomeResponsive(_:)``

Web プロセスが応答状態に戻ったことを通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewWebProcessDidBecomeResponsive:(WKWebView *)webView;
```

## Discussion
processDidBecomeResponsive で delegate を確認して呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L78)
- [`NavigationState.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
