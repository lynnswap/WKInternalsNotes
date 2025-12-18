# ``WKInternalsNotes/WKUserContentController/_removeAllUserContentFilters()``

登録済み user content filter を全削除する。

## Objective-C Declaration
```objective-c
- (void)_removeAllUserContentFilters WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Discussion
`ENABLE(CONTENT_EXTENSIONS)` が有効な場合に `removeAllContentRuleLists` を呼び出す。

## References
- [`WKUserContentControllerPrivate.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L45)
- [`WKUserContentController.mm#L287`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L287)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
