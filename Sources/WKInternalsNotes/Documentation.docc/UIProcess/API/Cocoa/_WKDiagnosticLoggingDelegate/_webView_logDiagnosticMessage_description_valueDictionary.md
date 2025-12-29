# ``WKInternalsNotes/_WKDiagnosticLoggingDelegate/_webView(_:logDiagnosticMessage:description:valueDictionary:)``

辞書付きの診断ログ通知。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView logDiagnosticMessage:(NSString *)message description:(NSString *)description valueDictionary:(NSDictionary *)valueDictionary WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
`DiagnosticLoggingClient` が `API::Dictionary` を `NSDictionary` に変換して渡す。`respondsToSelector:` を確認して呼び出す。

## References
- [`_WKDiagnosticLoggingDelegate.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDiagnosticLoggingDelegate.h#L47)
- [`DiagnosticLoggingClient.mm#L114`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/DiagnosticLoggingClient.mm#L114)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
