# ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate/_webExtensionController(_:receivedTestMessage:withArgument:andSourceURL:lineNumber:)``

browser.test.sendMessage のメッセージと引数を通知する。

## Objective-C Declaration
```objective-c
- (void)_webExtensionController:(WKWebExtensionController *)controller receivedTestMessage:(NSString *)message withArgument:(id)argument andSourceURL:(NSString *)sourceURL lineNumber:(unsigned)lineNumber;
```

## Discussion
`WebExtensionController::testSentMessage` で delegate が実装していれば呼び出し、`argument` は `parseJSON(..., FragmentsAllowed)` で変換した値が渡される。未実装時は message と argument をログ出力する。

## References
- [`WKWebExtensionControllerDelegatePrivate.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerDelegatePrivate.h#L61)
- [`WebExtensionControllerAPITestCocoa.mm#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionControllerAPITestCocoa.mm#L97)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
