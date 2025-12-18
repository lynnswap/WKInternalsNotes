# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:requestGeolocationPermissionForOrigin:initiatedByFrame:decisionHandler:)``

オリジンとフレーム情報付きで位置情報許可を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView requestGeolocationPermissionForOrigin:(WKSecurityOrigin*)origin initiatedByFrame:(WKFrameInfo *)frame decisionHandler:(void (^)(WKPermissionDecision decision))decisionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
UIDelegate::UIClient が `WKSecurityOrigin` と `WKFrameInfo` を渡して decisionHandler を呼び出す。

## References
- [`WKUIDelegatePrivate.h#L176`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L176)
- [`UIDelegate.mm#L612`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L612)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
