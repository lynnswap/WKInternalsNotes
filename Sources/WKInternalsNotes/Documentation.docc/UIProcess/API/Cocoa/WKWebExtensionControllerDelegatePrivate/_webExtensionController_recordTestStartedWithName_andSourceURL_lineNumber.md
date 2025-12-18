# ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate/_webExtensionController(_:recordTestStartedWithName:andSourceURL:lineNumber:)``

browser.test.addTest の開始を通知する。

## Objective-C Declaration
```objective-c
- (void)_webExtensionController:(WKWebExtensionController *)controller recordTestStartedWithName:(NSString *)testName andSourceURL:(NSString *)sourceURL lineNumber:(unsigned)lineNumber;
```

## Discussion
`WebExtensionController::testStarted` で delegate が実装していれば呼び出し、未実装時は開始ログを出力する。

## References
- [`WKWebExtensionControllerDelegatePrivate.h#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerDelegatePrivate.h#L73)
- [`WebExtensionControllerAPITestCocoa.mm#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionControllerAPITestCocoa.mm#L119)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
