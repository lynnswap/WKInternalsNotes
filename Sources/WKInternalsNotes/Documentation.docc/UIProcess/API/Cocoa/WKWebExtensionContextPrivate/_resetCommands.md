# ``WKInternalsNotes/WKWebExtensionContext/_resetCommands()``

コマンドを manifest の状態に戻す。

## Objective-C Declaration
```objective-c
- (void)_resetCommands;
```

## Discussion
`_webExtensionContext->resetCommands()` を呼ぶ。`ENABLE(WK_WEB_EXTENSIONS)` 無効時は何もしない。

## References
- [`WKWebExtensionContextPrivate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContextPrivate.h#L63)
- [`WKWebExtensionContext.mm#L581`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L581)
- [`WKWebExtensionContext.mm#L581`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L581)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
