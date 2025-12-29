# ``WKInternalsNotes/_WKDiagnosticLoggingDelegate/_webView(_:logDiagnosticMessageWithDomain:domain:)``

ドメイン付きの診断ログ通知。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView logDiagnosticMessageWithDomain:(NSString *)message domain:(_WKDiagnosticLoggingDomain)domain WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`DiagnosticLoggingClient` が `WebCore::DiagnosticLoggingDomain` を `_WKDiagnosticLoggingDomain` に変換して渡す。`respondsToSelector:` を確認して呼び出す。

## References
- [`_WKDiagnosticLoggingDelegate.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDiagnosticLoggingDelegate.h#L47)
- [`DiagnosticLoggingClient.mm#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/DiagnosticLoggingClient.mm#L121)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
