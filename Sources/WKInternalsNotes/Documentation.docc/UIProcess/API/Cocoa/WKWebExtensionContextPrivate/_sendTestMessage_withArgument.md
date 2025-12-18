# ``WKInternalsNotes/WKWebExtensionContext/_sendTestMessage(_:withArgument:)``

テスト用に `browser.test.onMessage` へメッセージを送る。

## Objective-C Declaration
```objective-c
- (void)_sendTestMessage:(NSString *)message withArgument:(nullable id)argument;
```

## Discussion
`message` が `NSString` であることを `NSParameterAssert` で検証し、`_protectedWebExtensionContext->sendTestMessage(message, argument)` を呼ぶ。`ENABLE(WK_WEB_EXTENSIONS)` 無効時は何もしない。

## References
- [`WKWebExtensionContextPrivate.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContextPrivate.h#L46)
- [`WKWebExtensionContext.mm#L855`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L855)
- [`WKWebExtensionContext.mm#L1292`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L1292)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
