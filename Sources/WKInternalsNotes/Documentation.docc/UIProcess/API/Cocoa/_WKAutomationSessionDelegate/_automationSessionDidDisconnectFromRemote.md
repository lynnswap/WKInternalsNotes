# ``WKInternalsNotes/_WKAutomationSessionDelegate/_automationSessionDidDisconnectFromRemote(_:)``

リモート接続の切断を通知する。

## Objective-C Declaration
```objective-c
- (void)_automationSessionDidDisconnectFromRemote:(_WKAutomationSession *)automationSession;
```

## Discussion
`AutomationSessionClient::didDisconnectFromRemote` から呼び出される。

## References
- [`_WKAutomationSessionDelegate.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionDelegate.h#L61)
- [`AutomationSessionClient.mm#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationSessionClient.mm#L63)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
