# ``WKInternalsNotes/_WKAutomationSessionDelegate/_automationSession(_:setUserInput:forCurrentJavaScriptDialogForWebView:)``

現在のJavaScriptダイアログに入力値を設定する。

## Objective-C Declaration
```objective-c
- (void)_automationSession:(_WKAutomationSession *)automationSession setUserInput:(NSString *)value forCurrentJavaScriptDialogForWebView:(WKWebView *)webView WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
`AutomationSessionClient::setUserInputForCurrentJavaScriptPromptOnPage` から呼び出される。

## References
- [`_WKAutomationSessionDelegate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionDelegate.h#L63)
- [`AutomationSessionClient.mm#L211`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationSessionClient.mm#L211)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
