# ``WKInternalsNotes/_WKDiagnosticLoggingDelegate/_webView(_:logDiagnosticMessage:description:)``

診断ログの基本メッセージ通知。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView logDiagnosticMessage:(NSString *)message description:(NSString *)description;
```

## Discussion
`DiagnosticLoggingClient` が `respondsToSelector:` を確認した上で呼び出し、`message` と `description` をそのまま渡す。

## References
- [`_WKDiagnosticLoggingDelegate.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDiagnosticLoggingDelegate.h#L47)
- [`DiagnosticLoggingClient.mm#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/DiagnosticLoggingClient.mm#L64)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
