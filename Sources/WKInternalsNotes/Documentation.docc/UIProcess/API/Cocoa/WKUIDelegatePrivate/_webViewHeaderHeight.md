# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewHeaderHeight(_:)``

印刷時ヘッダの高さを delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (CGFloat)_webViewHeaderHeight:(WKWebView *)webView WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
UIDelegate::UIClient が delegate からヘッダの高さを取得し、未実装時は 0 を返す。

## References
- [`WKUIDelegatePrivate.h#L324`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L324)
- [`UIDelegate.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
