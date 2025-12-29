# ``WKInternalsNotes/_WKDiagnosticLoggingDelegate/_webView(_:logDiagnosticMessageWithValue:description:value:)``

値付きの診断ログ通知。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView logDiagnosticMessageWithValue:(NSString *)message description:(NSString *)description value:(NSString *) value;
```

## Discussion
`DiagnosticLoggingClient` が `respondsToSelector:` を確認して呼び出し、`value` を文字列として渡す。

## References
- [`_WKDiagnosticLoggingDelegate.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDiagnosticLoggingDelegate.h#L47)
- [`DiagnosticLoggingClient.mm#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/DiagnosticLoggingClient.mm#L100)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
