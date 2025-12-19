# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webViewWebProcessDidCrash(_:)``

Web プロセスのクラッシュを通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewWebProcessDidCrash:(WKWebView *)webView;
```

## Discussion
`webContentProcessDidTerminateWithReason` が利用できない場合のフォールバックとして呼び出される。

## References
- [`WKNavigationDelegatePrivate.h#L77`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L77)
- [`NavigationState.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
