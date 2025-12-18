# ``WKInternalsNotes/_WKUserContentExtensionStore/storeWithURL(_:)``

指定 URL のストア領域を使うコンテンツ拡張ストアを作成する。

## Objective-C Declaration
```objective-c
+ (instancetype)storeWithURL:(NSURL *)url;
```

## Discussion
`WKContentRuleListStore storeWithURLAndLegacyFilename:` で store を作成し、`_initWithWKContentRuleListStore:` でラップして返す。

## References
- [`_WKUserContentExtensionStore.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.h#L35)
- [`_WKUserContentExtensionStore.mm#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentExtensionStore.mm#L69)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
