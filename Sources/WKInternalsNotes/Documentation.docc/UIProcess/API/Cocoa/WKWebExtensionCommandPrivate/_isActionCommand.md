# ``WKInternalsNotes/WKWebExtensionCommand/_isActionCommand``

このコマンドがアクションコマンドかどうかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _isActionCommand;
```

## Default Value
`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `NO`。有効時は `isActionCommand()` の結果。

## Discussion
`_protectedWebExtensionCommand->isActionCommand()` を返す。

## References
- [`WKWebExtensionCommandPrivate.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommandPrivate.h#L45)
- [`WKWebExtensionCommand.mm#L143`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommand.mm#L143)
- [`WKWebExtensionCommand.mm#L143`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommand.mm#L143)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
