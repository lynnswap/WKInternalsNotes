# ``WKInternalsNotes/_WKUserContentExtensionStore/_initWithWKContentRuleListStore(_:)``

既存の WKContentRuleListStore を用いてインスタンスを初期化する。

## Objective-C Declaration
```objective-c
- (id)_initWithWKContentRuleListStore:(WKContentRuleListStore *)contentRuleListStore WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
`[super init]` 後に `_contentRuleListStore` を設定して返す。`defaultStore` と `storeWithURL:` はこの初期化子で store を注入する。

## References
- [`_WKUserContentExtensionStorePrivate.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStorePrivate.h#L36)
- [`_WKUserContentExtensionStore.mm#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm#L123)
- [`_WKUserContentExtensionStore.mm#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm#L123)
- [`_WKUserContentExtensionStore.mm#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm#L123)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
