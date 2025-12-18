# ``WKInternalsNotes/_WKUserContentExtensionStore/_invalidateContentExtensionVersionForIdentifier(_:)``

指定 identifier のコンテンツ拡張のバージョンを無効化する（テスト用）。

## Objective-C Declaration
```objective-c
- (void)_invalidateContentExtensionVersionForIdentifier:(NSString *)identifier;
```

## Discussion
`_contentRuleListStore` の `_invalidateContentRuleListVersionForIdentifier:` に委譲し、保存済み rule list のバージョン情報を無効化する。

## References
- [`_WKUserContentExtensionStorePrivate.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStorePrivate.h#L34)
- [`_WKUserContentExtensionStore.mm#L118`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm#L118)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
