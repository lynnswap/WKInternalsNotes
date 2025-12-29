# ``WKInternalsNotes/_WKAutomationDelegate/_processPoolAllowsRemoteAutomation(_:)``

リモートオートメーションの許可可否を返す。

## Objective-C Declaration
```objective-c
- (BOOL)_processPoolAllowsRemoteAutomation:(WKProcessPool *)processPool WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
`AutomationClient::remoteAutomationAllowed` から呼び出され、未実装の場合は `false` が使われる。

## References
- [`_WKAutomationDelegate.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationDelegate.h#L35)
- [`AutomationClient.mm#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationClient.mm#L69)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
