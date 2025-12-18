# ``WKInternalsNotes/WKUserContentController/_addContentRuleList(_:extensionBaseURL:)``

ContentRuleList を user content controller に追加する。

## Objective-C Declaration
```objective-c
- (void)_addContentRuleList:(WKContentRuleList *)contentRuleList extensionBaseURL:(NSURL *)extensionBaseURL WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`ENABLE(CONTENT_EXTENSIONS)` が有効な場合に `addContentRuleList` を呼び出し、extension の base URL を渡す。

## References
- [`WKUserContentControllerPrivate.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L46)
- [`WKUserContentController.mm#L273`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L273)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
