# ``WKInternalsNotes/_WKAutomationSessionDelegate/_automationSession(_:acceptCurrentJavaScriptDialogForWebView:)``

自動化セッションから現在のJavaScriptダイアログを受け入れるよう通知する。

## Objective-C Declaration
```objective-c
- (void)_automationSession:(_WKAutomationSession *)automationSession acceptCurrentJavaScriptDialogForWebView:(WKWebView *)webView WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
`AutomationSessionClient::acceptCurrentJavaScriptDialogOnPage` から、対象の `WKWebView` がある場合に呼び出される。

## References
- [`_WKAutomationSessionDelegate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionDelegate.h#L63)
- [`AutomationSessionClient.mm#L183`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationSessionClient.mm#L183)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
