# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:requestDisplayCapturePermissionForOrigin:initiatedByFrame:withSystemAudio:decisionHandler:)``

画面キャプチャ許可を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView requestDisplayCapturePermissionForOrigin:(WKSecurityOrigin *)securityOrigin initiatedByFrame:(WKFrameInfo *)frame withSystemAudio:(BOOL)withSystemAudio decisionHandler:(void (^)(WKDisplayCapturePermissionDecision decision))decisionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
UIClient がトップレベルオリジンと `WKFrameInfo` を用意し、システム音声付き要求かどうかを `withSystemAudio` で渡して決定を受け取る。

## References
- [`WKUIDelegatePrivate.h#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L141)
- [`UIDelegate.mm#L1298`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1298)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
