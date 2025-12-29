# ``WKInternalsNotes/_WKAutomationSessionDelegate/_automationSession(_:loadWebExtensionWithOptions:resource:completionHandler:)``

Web拡張の読み込みを要求する。

## Objective-C Declaration
```objective-c
- (void)_automationSession:(_WKAutomationSession *)automationSession loadWebExtensionWithOptions:(_WKAutomationSessionWebExtensionResourceOptions)options resource:(NSString *)resource completionHandler:(void(^)(NSString *))completionHandler WK_API_AVAILABLE(macos(15.4));
```

## Discussion
`AutomationSessionClient::loadWebExtensionWithOptions` から呼び出され、拡張の識別子を `completionHandler` で返す。デリゲート未実装時は空文字列を返す。

## References
- [`_WKAutomationSessionDelegate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionDelegate.h#L63)
- [`AutomationSessionClient.mm#L142`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationSessionClient.mm#L142)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
