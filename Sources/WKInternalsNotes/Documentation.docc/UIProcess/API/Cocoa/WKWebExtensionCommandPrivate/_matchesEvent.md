# ``WKInternalsNotes/WKWebExtensionCommand/_matchesEvent(_:)``

イベントがコマンドのショートカットに一致するか判定する。

## Objective-C Declaration
```objective-c
- (BOOL)_matchesEvent:(NSEvent *)event;
```

## Discussion
macOS のみで有効（`TARGET_OS_OSX` / `USE(APPKIT)`）。`NSEvent` の型を `NSParameterAssert` で検証し、`matchesEvent(event)` を呼ぶ。`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `NO`。

## References
- [`WKWebExtensionCommandPrivate.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommandPrivate.h#L55)
- [`WKWebExtensionCommand.mm#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommand.mm#L149)
- [`WKWebExtensionCommand.mm#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommand.mm#L149)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
