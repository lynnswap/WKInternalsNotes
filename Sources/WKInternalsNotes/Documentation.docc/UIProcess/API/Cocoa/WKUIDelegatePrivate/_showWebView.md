# ``WKInternalsNotes/WKUIDelegatePrivate/_showWebView(_:)``

WebView の表示を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_showWebView:(WKWebView *)webView WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
UIClient の `showPage` から `_showWebView` を呼び出す。

## References
- [`WKUIDelegatePrivate.h#L316`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L316)
- [`UIDelegate.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
