# ``WKInternalsNotes/WKUserContentController/_removeUserScript(_:)``

user script を削除する。

## Objective-C Declaration
```objective-c
- (void)_removeUserScript:(WKUserScript *)userScript WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
`removeUserScript` に `WKUserScript` の内部表現を渡して削除する。

## References
- [`WKUserContentControllerPrivate.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L36)
- [`WKUserContentController.mm#L248`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L248)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
