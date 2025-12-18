# ``WKInternalsNotes/WKUserContentController/_removeUserContentFilter(_:)``

名前指定で user content filter を削除する。

## Objective-C Declaration
```objective-c
- (void)_removeUserContentFilter:(NSString *)userContentFilterName WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Discussion
`ENABLE(CONTENT_EXTENSIONS)` が有効な場合に `removeContentRuleList` を呼び出す。

## References
- [`WKUserContentControllerPrivate.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L44)
- [`WKUserContentController.mm#L280`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L280)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
