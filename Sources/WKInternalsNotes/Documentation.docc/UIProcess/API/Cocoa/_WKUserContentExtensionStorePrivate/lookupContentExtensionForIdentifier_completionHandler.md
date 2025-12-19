# ``WKInternalsNotes/_WKUserContentExtensionStore/lookupContentExtensionForIdentifier(_:completionHandler:)``

identifier で content extension を検索し、_WKUserContentFilter を返す。

## Objective-C Declaration
```objective-c
- (void)lookupContentExtensionForIdentifier:(NSString *)identifier completionHandler:(void (^)(_WKUserContentFilter *, NSError *))completionHandler;
```

## Discussion
`_contentRuleListStore` の lookUp を呼び、結果の `WKContentRuleList` を `_WKUserContentFilter` にラップして返す。エラーは `toUserContentRuleListStoreError` で変換される。

## References
- [`_WKUserContentExtensionStore.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.h#L38)
- [`_WKUserContentExtensionStore.mm#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm#L82)
- [`_WKUserContentExtensionStore.mm#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm#L82)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
