# ``WKInternalsNotes/_WKAutomationSessionDelegate/_automationSession(_:requestSwitchToWebView:completionHandler:)``

指定WebViewへの切り替えを要求する。

## Objective-C Declaration
```objective-c
- (void)_automationSession:(_WKAutomationSession *)automationSession requestSwitchToWebView:(WKWebView *)webView completionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`AutomationSessionClient::requestSwitchToPage` から呼び出され、`WKWebView` が取得できない場合は `completionHandler` が即時実行される。

## References
- [`_WKAutomationSessionDelegate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionDelegate.h#L63)
- [`AutomationSessionClient.mm#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationSessionClient.mm#L109)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
