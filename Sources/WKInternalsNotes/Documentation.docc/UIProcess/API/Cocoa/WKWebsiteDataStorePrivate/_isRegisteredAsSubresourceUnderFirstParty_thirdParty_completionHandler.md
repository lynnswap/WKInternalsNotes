# ``WKInternalsNotes/WKWebsiteDataStore/_isRegisteredAsSubresourceUnderFirstParty(_:thirdParty:completionHandler:)``

第一者/第三者関係がサブリソースとして登録済みか確認する。

## Objective-C Declaration
```objective-c
- (void)_isRegisteredAsSubresourceUnderFirstParty:(NSURL *)firstPartyURL thirdParty:(NSURL *)thirdPartyURL completionHandler:(void (^)(BOOL))completionHandler WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
第三者URL→第一者URLの順で `isRegisteredAsSubresourceUnder` を呼び、結果を `completionHandler` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L90)
- [`WKWebsiteDataStore.mm#L1070`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1070)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
