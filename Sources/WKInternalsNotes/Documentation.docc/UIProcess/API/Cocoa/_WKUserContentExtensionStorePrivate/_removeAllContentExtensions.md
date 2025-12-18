# ``WKInternalsNotes/_WKUserContentExtensionStore/_removeAllContentExtensions()``

全コンテンツ拡張を削除する（テスト用）。

## Objective-C Declaration
```objective-c
- (void)_removeAllContentExtensions;
```

## Discussion
`_contentRuleListStore` の `_removeAllContentRuleLists` に委譲して、全 rule list を削除する。

## References
- [`_WKUserContentExtensionStorePrivate.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStorePrivate.h#L33)
- [`_WKUserContentExtensionStore.mm#L113`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm#L113)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
