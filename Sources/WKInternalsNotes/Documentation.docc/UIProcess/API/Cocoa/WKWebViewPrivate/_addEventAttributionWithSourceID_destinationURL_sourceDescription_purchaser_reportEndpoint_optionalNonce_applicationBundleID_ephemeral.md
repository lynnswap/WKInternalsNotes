# ``WKInternalsNotes/WKWebView/_addEventAttributionWithSourceID(_:destinationURL:sourceDescription:purchaser:reportEndpoint:optionalNonce:applicationBundleID:ephemeral:)``

`_addEventAttributionWithSourceID` を追加する。

## Objective-C Declaration
```objective-c
- (void)_addEventAttributionWithSourceID:(uint8_t)sourceID destinationURL:(NSURL *)destination sourceDescription:(NSString *)sourceDescription purchaser:(NSString *)purchaser reportEndpoint:(NSURL *)reportEndpoint optionalNonce:(nullable NSString *)nonce applicationBundleID:(NSString *)bundleID ephemeral:(BOOL)ephemeral WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L60)
- [`API/Cocoa/WKWebViewTesting.mm#L208`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L208)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
