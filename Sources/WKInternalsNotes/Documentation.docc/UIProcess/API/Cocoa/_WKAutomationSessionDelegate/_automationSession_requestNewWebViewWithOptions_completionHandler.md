# ``WKInternalsNotes/_WKAutomationSessionDelegate/_automationSession(_:requestNewWebViewWithOptions:completionHandler:)``

新しい `WKWebView` の作成を要求する。

## Objective-C Declaration
```objective-c
- (void)_automationSession:(_WKAutomationSession *)automationSession requestNewWebViewWithOptions:(_WKAutomationSessionBrowsingContextOptions)options completionHandler:(void(^)(WKWebView * _Nullable))completionHandler WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`AutomationSessionClient::requestNewPageWithOptions` から呼び出され、`completionHandler` で返された `WKWebView` からページを取得する。

## References
- [`_WKAutomationSessionDelegate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionDelegate.h#L63)
- [`AutomationSessionClient.mm#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationSessionClient.mm#L99)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
