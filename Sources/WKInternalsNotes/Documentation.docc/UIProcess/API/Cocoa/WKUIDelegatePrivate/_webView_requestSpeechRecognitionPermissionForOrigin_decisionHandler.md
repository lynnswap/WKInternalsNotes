# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:requestSpeechRecognitionPermissionForOrigin:decisionHandler:)``

音声認識の許可を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView requestSpeechRecognitionPermissionForOrigin:(WKSecurityOrigin *)origin decisionHandler:(void (^)(BOOL authorized))decisionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
現行の UIProcess 実装では呼び出し箇所が見当たらず、宣言のみが存在する。

## References
- [`WKUIDelegatePrivate.h#L202`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L202)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
