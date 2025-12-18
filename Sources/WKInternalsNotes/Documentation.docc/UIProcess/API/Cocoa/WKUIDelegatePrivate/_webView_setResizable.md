# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:setResizable:)``

WebView のリサイズ可否を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView setResizable:(BOOL)isResizable WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
UIDelegate::UIClient が window feature 由来の resizable 情報を delegate へ渡す。

## References
- [`WKUIDelegatePrivate.h#L329`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L329)
- [`UIDelegate.mm#L1114`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1114)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
