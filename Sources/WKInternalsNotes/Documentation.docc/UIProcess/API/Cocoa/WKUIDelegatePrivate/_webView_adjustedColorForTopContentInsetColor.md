# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:adjustedColorForTopContentInsetColor:)``

トップコンテンツインセットの色を delegate が調整する。

## Objective-C Declaration
```objective-c
- (NSColor *)_webView:(WKWebView *)webView adjustedColorForTopContentInsetColor:(NSColor *)proposedColor WK_API_AVAILABLE(macos(26.0));
```

## Discussion
WKWebView が delegate に色の調整を問い合わせ、未実装時は元の色を返す。delegate が `nil` を返した場合も元の色にフォールバックする。

## References
- [`WKUIDelegatePrivate.h#L355`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L355)
- [`WKWebView.mm#L3386`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3386)
- [`WKWebView.mm#L3391`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3391)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
