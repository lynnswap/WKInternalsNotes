# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:requestGeolocationPermissionForFrame:decisionHandler:)``

フレーム単位の位置情報許可を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView requestGeolocationPermissionForFrame:(WKFrameInfo *)frame decisionHandler:(void (^)(BOOL allowed))decisionHandler WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
UIDelegate::UIClient で origin-based API が未実装の場合のフォールバックとして呼び出される。

## References
- [`WKUIDelegatePrivate.h#L158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L158)
- [`UIDelegate.mm#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L135)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
