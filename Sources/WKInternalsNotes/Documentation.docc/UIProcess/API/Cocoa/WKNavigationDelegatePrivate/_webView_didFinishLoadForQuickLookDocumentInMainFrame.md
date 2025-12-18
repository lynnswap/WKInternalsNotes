# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:didFinishLoadForQuickLookDocumentInMainFrame:)``

Quick Look ドキュメントの読み込み完了を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didFinishLoadForQuickLookDocumentInMainFrame:(NSData *)documentData;
```

## Discussion
didFinishLoadForQuickLookDocumentInMainFrame でバッファを NSData に変換して渡す。

## References
- [`WKNavigationDelegatePrivate.h#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L117)
- [`NavigationState.mm#L1441`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L1441)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
