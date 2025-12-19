# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:takeFocus:)``

WebView がフォーカスを取る処理を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView takeFocus:(_WKFocusDirection)direction WK_API_AVAILABLE(macos(10.13.4), ios(12.2));
```

## Discussion
UIDelegate::UIClient が `WKFocusDirection` を渡して delegate に通知し、処理できたかどうかを返す。

## References
- [`WKUIDelegatePrivate.h#L169`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L169)
- [`UIDelegate.mm#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L135)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
