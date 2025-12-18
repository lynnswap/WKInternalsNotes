# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:navigationDidFinishDocumentLoad:)``

ドキュメントロード完了を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView navigationDidFinishDocumentLoad:(WKNavigation *)navigation;
```

## Discussion
didFinishDocumentLoad で WKNavigation を渡して呼び出す。

## References
- [`WKNavigationDelegatePrivate.h#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L72)
- [`NavigationState.mm#L1018`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L1018)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
