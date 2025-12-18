# ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate/_webExtensionController(_:recordTestAssertionResult:withMessage:andSourceURL:lineNumber:)``

browser.test.assertTrue/False/Throws/Rejects の結果を通知する。

## Objective-C Declaration
```objective-c
- (void)_webExtensionController:(WKWebExtensionController *)controller recordTestAssertionResult:(BOOL)result withMessage:(NSString *)message andSourceURL:(NSString *)sourceURL lineNumber:(unsigned)lineNumber;
```

## Discussion
`WebExtensionController::testResult` で delegate が実装していれば呼び出し、未実装時は `message` が空なら `(no message)` を補正して結果に応じてログを出力する。

## References
- [`WKWebExtensionControllerDelegatePrivate.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerDelegatePrivate.h#L43)
- [`WebExtensionControllerAPITestCocoa.mm#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionControllerAPITestCocoa.mm#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
