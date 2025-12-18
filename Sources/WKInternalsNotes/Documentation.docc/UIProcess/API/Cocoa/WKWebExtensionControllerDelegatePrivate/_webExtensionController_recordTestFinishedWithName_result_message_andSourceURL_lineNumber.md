# ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate/_webExtensionController(_:recordTestFinishedWithName:result:message:andSourceURL:lineNumber:)``

browser.test.notifyPass/Fail の結果を通知する。

## Objective-C Declaration
```objective-c
- (void)_webExtensionController:(WKWebExtensionController *)controller recordTestFinishedWithName:(NSString *)testName result:(BOOL)result message:(NSString *)message andSourceURL:(NSString *)sourceURL lineNumber:(unsigned)lineNumber;
```

## Discussion
`WebExtensionController::testFinished` で delegate が実装していれば呼び出し、未実装時は `testName` / `message` が空なら `(no test name)` / `(no message)` を補正して結果に応じてログ出力する。

## References
- [`WKWebExtensionControllerDelegatePrivate.h#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerDelegatePrivate.h#L80)
- [`WebExtensionControllerAPITestCocoa.mm#L130`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionControllerAPITestCocoa.mm#L130)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
