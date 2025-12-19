# ``WKInternalsNotes/WKWebExtensionContext/_sendTestStartedWithArgument(_:)``

テスト用に `browser.test.onTestStarted` を送信する。

## Objective-C Declaration
```objective-c
- (void)_sendTestStartedWithArgument:(nullable id)argument;
```

## Discussion
`_protectedWebExtensionContext->sendTestStarted(argument)` を呼ぶ。`ENABLE(WK_WEB_EXTENSIONS)` 無効時は何もしない。

## References
- [`WKWebExtensionContextPrivate.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContextPrivate.h#L53)
- [`WKWebExtensionContext.mm#L862`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L862)
- [`WKWebExtensionContext.mm#L862`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L862)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
