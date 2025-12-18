# ``WKInternalsNotes/WKUserContentController/_addUserStyleSheet(_:)``

User style sheet を追加する。

## Objective-C Declaration
```objective-c
- (void)_addUserStyleSheet:(_WKUserStyleSheet *)userStyleSheet WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
`_WKUserStyleSheet` の内部表現を `addUserStyleSheet` に渡す。

## References
- [`WKUserContentControllerPrivate.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L49)
- [`WKUserContentController.mm#L299`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L299)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
