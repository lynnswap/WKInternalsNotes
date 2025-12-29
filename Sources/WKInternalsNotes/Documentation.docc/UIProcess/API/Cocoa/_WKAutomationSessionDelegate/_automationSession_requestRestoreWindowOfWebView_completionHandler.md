# ``WKInternalsNotes/_WKAutomationSessionDelegate/_automationSession(_:requestRestoreWindowOfWebView:completionHandler:)``

対象WebViewのウィンドウ復帰を要求する。

## Objective-C Declaration
```objective-c
- (void)_automationSession:(_WKAutomationSession *)automationSession requestRestoreWindowOfWebView:(WKWebView *)webView completionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`AutomationSessionClient::requestRestoreWindowOfPage` から呼び出され、`WKWebView` が取得できない場合は即座に完了する。

## References
- [`_WKAutomationSessionDelegate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionDelegate.h#L63)
- [`AutomationSessionClient.mm#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationSessionClient.mm#L125)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
