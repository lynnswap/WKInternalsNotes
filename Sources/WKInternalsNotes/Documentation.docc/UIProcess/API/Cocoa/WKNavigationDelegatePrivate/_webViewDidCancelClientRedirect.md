# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webViewDidCancelClientRedirect(_:)``

クライアントリダイレクトのキャンセルを通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewDidCancelClientRedirect:(WKWebView *)webView;
```

## Discussion
didCancelClientRedirect で delegate を確認して呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L70)
- [`NavigationState.mm#L920`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L920)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
