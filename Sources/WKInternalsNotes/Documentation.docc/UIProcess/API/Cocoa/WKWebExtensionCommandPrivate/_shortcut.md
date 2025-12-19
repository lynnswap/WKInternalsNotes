# ``WKInternalsNotes/WKWebExtensionCommand/_shortcut``

拡張コマンドのショートカット文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *_shortcut;
```

## Default Value
`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `nil`。有効時は内部 `shortcutString()` の結果（ショートカット未設定時は空文字列）。

## Discussion
`_protectedWebExtensionCommand->shortcutString()` を文字列化して返す。

## References
- [`WKWebExtensionCommandPrivate.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommandPrivate.h#L35)
- [`WKWebExtensionCommand.mm#L133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommand.mm#L133)
- [`WKWebExtensionCommand.mm#L133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommand.mm#L133)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
