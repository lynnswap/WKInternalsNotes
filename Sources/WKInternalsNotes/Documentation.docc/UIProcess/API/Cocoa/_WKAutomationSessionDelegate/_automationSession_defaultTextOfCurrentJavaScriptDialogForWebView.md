# ``WKInternalsNotes/_WKAutomationSessionDelegate/_automationSession(_:defaultTextOfCurrentJavaScriptDialogForWebView:)``

現在のJavaScriptダイアログのデフォルトテキストを返す。

## Objective-C Declaration
```objective-c
- (nullable NSString *)_automationSession:(_WKAutomationSession *)automationSession defaultTextOfCurrentJavaScriptDialogForWebView:(WKWebView *)webView WK_API_AVAILABLE(macos(26.0), ios(26.0), visionos(26.0));
```

## Discussion
`AutomationSessionClient::defaultTextOfCurrentJavaScriptDialogOnPage` から呼び出され、`WKWebView` がない場合は `nil` 扱いになる。

## References
- [`_WKAutomationSessionDelegate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionDelegate.h#L63)
- [`AutomationSessionClient.mm#L195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationSessionClient.mm#L195)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
