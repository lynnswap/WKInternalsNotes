# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:didStartLoadForQuickLookDocumentInMainFrameWithFileName:uti:)``

Quick Look ドキュメントの読み込み開始を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didStartLoadForQuickLookDocumentInMainFrameWithFileName:(NSString *)fileName uti:(NSString *)uti;
```

## Discussion
didStartLoadForQuickLookDocumentInMainFrame で fileName/uti を NSString に変換して渡す。

## References
- [`WKNavigationDelegatePrivate.h#L94`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L94)
- [`NavigationState.mm#L212`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L212)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
