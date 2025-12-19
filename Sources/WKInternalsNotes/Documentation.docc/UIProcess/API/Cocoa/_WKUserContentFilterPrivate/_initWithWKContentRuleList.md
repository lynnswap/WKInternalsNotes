# ``WKInternalsNotes/_WKUserContentFilter/_initWithWKContentRuleList(_:)``

WKContentRuleList を保持する _WKUserContentFilter を初期化する。

## Objective-C Declaration
```objective-c
- (id)_initWithWKContentRuleList:(WKContentRuleList*)contentRuleList WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
`[super init]` の後に `_contentRuleList` を設定して返す。`_WKUserContentExtensionStore` が生成した `WKContentRuleList` をラップする用途で使われる。

## References
- [`_WKUserContentFilterPrivate.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentFilterPrivate.h#L33)
- [`_WKUserContentFilterInternal.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentFilterInternal.h)
- [`_WKUserContentFilter.mm#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentFilter.mm#L54)
- [`_WKUserContentExtensionStore.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
