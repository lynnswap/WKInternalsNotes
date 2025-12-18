# ``WKInternalsNotes/_WKUserContentExtensionStore/_contentRuleListStore``

内部で利用する WKContentRuleListStore を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKContentRuleListStore *_contentRuleListStore WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Default Value
`_initWithWKContentRuleListStore:` で設定された `WKContentRuleListStore`。未初期化の場合は `nil`。

## Discussion
`_contentRuleListStore` の参照を返すだけで、実体は `_initWithWKContentRuleListStore:` で設定される。公開 API の compile/lookup/remove はこの store に委譲される。

## References
- [`_WKUserContentExtensionStorePrivate.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStorePrivate.h#L37)
- [`_WKUserContentExtensionStoreInternal.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStoreInternal.h#L35)
- [`_WKUserContentExtensionStore.mm#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm#L123)
- [`_WKUserContentExtensionStore.mm#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm#L134)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
