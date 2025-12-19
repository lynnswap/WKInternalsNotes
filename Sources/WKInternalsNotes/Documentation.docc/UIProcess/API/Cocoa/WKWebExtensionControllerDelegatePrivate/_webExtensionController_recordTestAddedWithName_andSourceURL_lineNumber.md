# ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate/_webExtensionController(_:recordTestAddedWithName:andSourceURL:lineNumber:)``

browser.test.addTest で追加されたテストを通知する。

## Objective-C Declaration
```objective-c
- (void)_webExtensionController:(WKWebExtensionController *)controller recordTestAddedWithName:(NSString *)testName andSourceURL:(NSString *)sourceURL lineNumber:(unsigned)lineNumber;
```

## Discussion
`WebExtensionController::testAdded` で delegate が実装していれば呼び出し、未実装時は追加ログを出力する。

## References
- [`WKWebExtensionControllerDelegatePrivate.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerDelegatePrivate.h#L43)
- [`WebExtensionControllerAPITestCocoa.mm#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionControllerAPITestCocoa.mm#L84)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
