# ``WKInternalsNotes/_WKUserContentExtensionStore/removeContentExtensionForIdentifier(_:completionHandler:)``

identifier で content extension を削除する。

## Objective-C Declaration
```objective-c
- (void)removeContentExtensionForIdentifier:(NSString *)identifier completionHandler:(void (^)(NSError *))completionHandler;
```

## Discussion
`_contentRuleListStore` の remove を呼び、完了時にエラーを `toUserContentRuleListStoreError` で変換して返す。

## References
- [`_WKUserContentExtensionStore.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.h#L39)
- [`_WKUserContentExtensionStore.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm#L39)
- [`_WKUserContentExtensionStore.mm#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm#L90)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
