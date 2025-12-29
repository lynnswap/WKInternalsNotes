# ``WKInternalsNotes/_WKAutomationSessionDelegate/_automationSession(_:isShowingJavaScriptDialogForWebView:)``

JavaScriptダイアログ表示中かを返す。

## Objective-C Declaration
```objective-c
- (BOOL)_automationSession:(_WKAutomationSession *)automationSession isShowingJavaScriptDialogForWebView:(WKWebView *)webView WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
`AutomationSessionClient::isShowingJavaScriptDialogOnPage` から呼び出され、未実装時は `false` が返る。

## References
- [`_WKAutomationSessionDelegate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionDelegate.h#L63)
- [`AutomationSessionClient.mm#L167`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationSessionClient.mm#L167)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
