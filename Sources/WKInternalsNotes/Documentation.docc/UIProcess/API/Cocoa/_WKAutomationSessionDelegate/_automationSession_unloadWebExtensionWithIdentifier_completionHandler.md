# ``WKInternalsNotes/_WKAutomationSessionDelegate/_automationSession(_:unloadWebExtensionWithIdentifier:completionHandler:)``

Web拡張のアンロードを要求する。

## Objective-C Declaration
```objective-c
- (void)_automationSession:(_WKAutomationSession *)automationSession unloadWebExtensionWithIdentifier:(NSString *)identifier completionHandler:(void(^)(BOOL))completionHandler WK_API_AVAILABLE(macos(15.4));
```

## Discussion
`AutomationSessionClient::unloadWebExtension` から呼び出され、未実装の場合は `completionHandler(false)` が実行される。

## References
- [`_WKAutomationSessionDelegate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionDelegate.h#L63)
- [`AutomationSessionClient.mm#L154`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationSessionClient.mm#L154)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
