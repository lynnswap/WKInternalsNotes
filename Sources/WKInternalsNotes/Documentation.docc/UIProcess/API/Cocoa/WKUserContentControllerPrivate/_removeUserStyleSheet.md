# ``WKInternalsNotes/WKUserContentController/_removeUserStyleSheet(_:)``

user style sheet を削除する。

## Objective-C Declaration
```objective-c
- (void)_removeUserStyleSheet:(_WKUserStyleSheet *)userStyleSheet WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
`removeUserStyleSheet` に内部表現を渡して削除する。

## References
- [`WKUserContentControllerPrivate.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L50)
- [`WKUserContentController.mm#L304`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L304)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
