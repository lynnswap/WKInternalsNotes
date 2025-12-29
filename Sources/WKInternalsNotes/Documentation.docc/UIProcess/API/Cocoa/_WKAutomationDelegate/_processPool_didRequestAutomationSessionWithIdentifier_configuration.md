# ``WKInternalsNotes/_WKAutomationDelegate/_processPool(_:didRequestAutomationSessionWithIdentifier:configuration:)``

オートメーションセッションの作成要求を通知する。

## Objective-C Declaration
```objective-c
- (void)_processPool:(WKProcessPool *)processPool didRequestAutomationSessionWithIdentifier:(NSString *)identifier configuration:(_WKAutomationSessionConfiguration *)configuration WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
`AutomationClient::requestAutomationSession` からメインスレッドにディスパッチされ、`sessionCapabilities` を反映した `configuration` を渡して呼び出される。

## References
- [`_WKAutomationDelegate.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationDelegate.h#L36)
- [`AutomationClient.mm#L77`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationClient.mm#L77)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
