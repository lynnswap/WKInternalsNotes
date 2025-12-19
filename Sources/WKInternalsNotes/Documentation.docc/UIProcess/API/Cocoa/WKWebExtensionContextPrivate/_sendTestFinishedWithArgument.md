# ``WKInternalsNotes/WKWebExtensionContext/_sendTestFinishedWithArgument(_:)``

テスト用に `browser.test.onTestFinished` を送信する。

## Objective-C Declaration
```objective-c
- (void)_sendTestFinishedWithArgument:(nullable id)argument;
```

## Discussion
`_protectedWebExtensionContext->sendTestFinished(argument)` を呼ぶ。`ENABLE(WK_WEB_EXTENSIONS)` 無効時は何もしない。

## References
- [`WKWebExtensionContextPrivate.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContextPrivate.h#L60)
- [`WKWebExtensionContext.mm#L867`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L867)
- [`WKWebExtensionContext.mm#L867`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L867)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
