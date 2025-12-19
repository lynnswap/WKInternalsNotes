# ``WKInternalsNotes/WKWebsiteDataStore/_isRelationshipOnlyInDatabaseOnce(_:thirdParty:completionHandler:)``

第一者/第三者関係がDBに1回のみ存在するか確認する。

## Objective-C Declaration
```objective-c
- (void)_isRelationshipOnlyInDatabaseOnce:(NSURL *)firstPartyURL thirdParty:(NSURL *)thirdPartyURL completionHandler:(void (^)(BOOL))completionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
第三者URL→第一者URLの順で `isRelationshipOnlyInDatabaseOnce` を呼び、結果を `completionHandler` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L89)
- [`WKWebsiteDataStore.mm#L1063`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1063)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
