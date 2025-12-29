# ``WKInternalsNotes/_WKAutomationSessionDelegate/_automationSession(_:dismissCurrentJavaScriptDialogForWebView:)``

現在のJavaScriptダイアログを閉じる。

## Objective-C Declaration
```objective-c
- (void)_automationSession:(_WKAutomationSession *)automationSession dismissCurrentJavaScriptDialogForWebView:(WKWebView *)webView WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
`AutomationSessionClient::dismissCurrentJavaScriptDialogOnPage` から呼び出され、`WKWebView` がない場合は何もしない。

## References
- [`_WKAutomationSessionDelegate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionDelegate.h#L63)
- [`AutomationSessionClient.mm#L175`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationSessionClient.mm#L175)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
