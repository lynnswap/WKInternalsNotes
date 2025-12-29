# ``WKInternalsNotes/_WKAutomationSessionDelegate/_automationSession(_:typeOfCurrentJavaScriptDialogForWebView:)``

現在のJavaScriptダイアログの種類を返す。

## Objective-C Declaration
```objective-c
- (_WKAutomationSessionJavaScriptDialogType)_automationSession:(_WKAutomationSession *)automationSession typeOfCurrentJavaScriptDialogForWebView:(WKWebView *)webView WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`AutomationSessionClient::typeOfCurrentJavaScriptDialogOnPage` から呼び出され、戻り値は内部の `JavaScriptDialogType` に変換される。未実装時は `Prompt` が使われる。

## References
- [`_WKAutomationSessionDelegate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionDelegate.h#L63)
- [`AutomationSessionClient.mm#L239`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationSessionClient.mm#L239)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
