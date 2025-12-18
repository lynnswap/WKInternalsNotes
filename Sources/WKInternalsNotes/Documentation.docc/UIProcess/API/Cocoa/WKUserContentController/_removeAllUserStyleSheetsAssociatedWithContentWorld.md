# ``WKInternalsNotes/WKUserContentController/_removeAllUserStyleSheetsAssociatedWithContentWorld(_:)``

指定 content world の user style sheet を全削除する。

## Objective-C Declaration
```objective-c
- (void)_removeAllUserStyleSheetsAssociatedWithContentWorld:(WKContentWorld *)contentWorld WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`removeAllUserStyleSheets` に content world を渡して削除する。

## References
- [`WKUserContentControllerPrivate.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L52)
- [`WKUserContentController.mm#L314`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L314)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
