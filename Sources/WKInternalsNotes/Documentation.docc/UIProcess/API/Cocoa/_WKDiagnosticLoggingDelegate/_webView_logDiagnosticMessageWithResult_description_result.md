# ``WKInternalsNotes/_WKDiagnosticLoggingDelegate/_webView(_:logDiagnosticMessageWithResult:description:result:)``

結果付きの診断ログ通知。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView logDiagnosticMessageWithResult:(NSString *)message description:(NSString *)description result:(_WKDiagnosticLoggingResultType)result;
```

## Discussion
`DiagnosticLoggingClient` が `result` を `_WKDiagnosticLoggingResultType` に変換し、`respondsToSelector:` を確認して呼び出す。

## References
- [`_WKDiagnosticLoggingDelegate.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDiagnosticLoggingDelegate.h#L47)
- [`DiagnosticLoggingClient.mm#L93`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/DiagnosticLoggingClient.mm#L93)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
