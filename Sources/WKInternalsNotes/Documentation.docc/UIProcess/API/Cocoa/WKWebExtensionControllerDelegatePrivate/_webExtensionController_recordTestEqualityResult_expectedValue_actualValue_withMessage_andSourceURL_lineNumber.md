# ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate/_webExtensionController(_:recordTestEqualityResult:expectedValue:actualValue:withMessage:andSourceURL:lineNumber:)``

browser.test.assertEq/assertDeepEq の結果を通知する。

## Objective-C Declaration
```objective-c
- (void)_webExtensionController:(WKWebExtensionController *)controller recordTestEqualityResult:(BOOL)result expectedValue:(NSString *)expectedValue actualValue:(NSString *)actualValue withMessage:(NSString *)message andSourceURL:(NSString *)sourceURL lineNumber:(unsigned)lineNumber;
```

## Discussion
`WebExtensionController::testEqual` で delegate が実装していれば呼び出し、未実装時は `message` が空なら "Expected equality of these values" を使って expected/actual とともにログ出力する。

## References
- [`WKWebExtensionControllerDelegatePrivate.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerDelegatePrivate.h#L49)
- [`WebExtensionControllerAPITestCocoa.mm#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionControllerAPITestCocoa.mm#L64)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
