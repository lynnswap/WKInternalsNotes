# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewRunModal(_:)``

WebView をモーダル実行するよう delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewRunModal:(WKWebView *)webView WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
UIDelegate::UIClient が `_webViewRunModal:` を呼び出し、モーダル表示の制御を delegate に委ねる。

## References
- [`WKUIDelegatePrivate.h#L320`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L320)
- [`UIDelegate.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
