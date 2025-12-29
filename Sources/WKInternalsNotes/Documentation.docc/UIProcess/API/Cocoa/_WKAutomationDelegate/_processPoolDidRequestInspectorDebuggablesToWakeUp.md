# ``WKInternalsNotes/_WKAutomationDelegate/_processPoolDidRequestInspectorDebuggablesToWakeUp(_:)``

インスペクタのデバッグ対象の起動要求を通知する。

## Objective-C Declaration
```objective-c
- (void)_processPoolDidRequestInspectorDebuggablesToWakeUp:(WKProcessPool *)processPool WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`AutomationClient::requestedDebuggablesToWakeUp` からメインスレッドにディスパッチされて呼び出される。

## References
- [`_WKAutomationDelegate.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationDelegate.h#L41)
- [`AutomationClient.mm#L102`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationClient.mm#L102)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
