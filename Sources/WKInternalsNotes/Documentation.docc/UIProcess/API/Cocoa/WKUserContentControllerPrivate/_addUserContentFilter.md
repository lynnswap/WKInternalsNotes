# ``WKInternalsNotes/WKUserContentController/_addUserContentFilter(_:)``

User content filter を追加する。

## Objective-C Declaration
```objective-c
- (void)_addUserContentFilter:(_WKUserContentFilter *)userContentFilter WK_API_DEPRECATED_WITH_REPLACEMENT("addContentRuleList", macos(10.11, 13.3), ios(9.0, 16.4));
```

## Discussion
`ENABLE(CONTENT_EXTENSIONS)` が有効な場合に `_WKUserContentFilter` の rule list を追加する。

## References
- [`WKUserContentControllerPrivate.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L42)
- [`WKUserContentController.mm#L265`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L265)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
