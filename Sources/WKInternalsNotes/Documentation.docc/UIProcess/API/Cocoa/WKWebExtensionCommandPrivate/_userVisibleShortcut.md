# ``WKInternalsNotes/WKWebExtensionCommand/_userVisibleShortcut``

ユーザ表示用のショートカット文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *_userVisibleShortcut;
```

## Default Value
`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `nil`。有効時は `userVisibleShortcut()` の結果。

## Discussion
`_protectedWebExtensionCommand->userVisibleShortcut()` を文字列化して返す。

## References
- [`WKWebExtensionCommandPrivate.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommandPrivate.h#L42)
- [`WKWebExtensionCommand.mm#L138`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommand.mm#L138)
- [`WKWebExtensionCommand.mm#L226`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommand.mm#L226)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
