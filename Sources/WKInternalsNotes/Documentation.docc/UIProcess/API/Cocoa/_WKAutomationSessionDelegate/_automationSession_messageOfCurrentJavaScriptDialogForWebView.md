# ``WKInternalsNotes/_WKAutomationSessionDelegate/_automationSession(_:messageOfCurrentJavaScriptDialogForWebView:)``

現在のJavaScriptダイアログのメッセージを返す。

## Objective-C Declaration
```objective-c
- (nullable NSString *)_automationSession:(_WKAutomationSession *)automationSession messageOfCurrentJavaScriptDialogForWebView:(WKWebView *)webView WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
`AutomationSessionClient::messageOfCurrentJavaScriptDialogOnPage` から呼び出され、`WKWebView` がない場合は `nil` 扱いになる。

## References
- [`_WKAutomationSessionDelegate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionDelegate.h#L63)
- [`AutomationSessionClient.mm#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationSessionClient.mm#L187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
