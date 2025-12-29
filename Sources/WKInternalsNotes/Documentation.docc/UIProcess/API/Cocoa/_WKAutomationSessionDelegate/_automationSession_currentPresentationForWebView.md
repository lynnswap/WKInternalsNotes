# ``WKInternalsNotes/_WKAutomationSessionDelegate/_automationSession(_:currentPresentationForWebView:)``

現在の表示形態（タブ/ウィンドウ）を返す。

## Objective-C Declaration
```objective-c
- (_WKAutomationSessionBrowsingContextPresentation)_automationSession:(_WKAutomationSession *)automationSession currentPresentationForWebView:(WKWebView *)webView WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
`AutomationSessionClient::currentPresentationOfPage` から呼び出され、未実装時は `Window` が使われる。

## References
- [`_WKAutomationSessionDelegate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionDelegate.h#L63)
- [`AutomationSessionClient.mm#L249`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationSessionClient.mm#L249)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
