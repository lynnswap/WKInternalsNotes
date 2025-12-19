# ``WKInternalsNotes/_WKUserContentExtensionStore/compileContentExtensionForIdentifier(_:encodedContentExtension:encodedContentExtension completionHandler:)``

エンコード済みの content extension をコンパイルし、_WKUserContentFilter として返す。

## Objective-C Declaration
```objective-c
- (void)compileContentExtensionForIdentifier:(NSString *)identifier encodedContentExtension:(NSString *) NS_RELEASES_ARGUMENT encodedContentExtension completionHandler:(void (^)(_WKUserContentFilter *, NSError *))completionHandler;
```

## Discussion
`_contentRuleListStore` の compile を呼び、生成された `WKContentRuleList` を `_WKUserContentFilter` にラップして返す。エラーは `toUserContentRuleListStoreError` で `_WKUserContentExtensionStoreErrorCode` に変換される。

## References
- [`_WKUserContentExtensionStore.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.h#L37)
- [`_WKUserContentExtensionStore.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm)
- [`_WKUserContentExtensionStore.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
