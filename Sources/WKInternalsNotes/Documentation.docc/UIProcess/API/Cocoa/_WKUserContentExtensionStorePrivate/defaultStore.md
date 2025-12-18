# ``WKInternalsNotes/_WKUserContentExtensionStore/defaultStore()``

既定のコンテンツ拡張ストアを返す。

## Objective-C Declaration
```objective-c
+ (instancetype)defaultStore;
```

## Discussion
`WKContentRuleListStore defaultStoreWithLegacyFilename` で store を取得し、`_initWithWKContentRuleListStore:` でラップして返す。

## References
- [`_WKUserContentExtensionStore.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.h#L34)
- [`_WKUserContentExtensionStore.mm#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm#L64)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
