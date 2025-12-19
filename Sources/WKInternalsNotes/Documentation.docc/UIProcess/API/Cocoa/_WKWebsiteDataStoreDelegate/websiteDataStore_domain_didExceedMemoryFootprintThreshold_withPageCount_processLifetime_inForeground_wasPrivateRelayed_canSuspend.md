# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/websiteDataStore(_:domain:didExceedMemoryFootprintThreshold:withPageCount:processLifetime:inForeground:wasPrivateRelayed:canSuspend:)``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
- (void)websiteDataStore:(WKWebsiteDataStore *)dataStore domain:(NSString *)registrableDomain didExceedMemoryFootprintThreshold:(size_t)footprint withPageCount:(NSUInteger)pageCount processLifetime:(NSTimeInterval)processLifetime inForeground:(BOOL)inForeground wasPrivateRelayed:(BOOL)wasPrivateRelayed canSuspend:(BOOL)canSuspend;
```

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`_WKWebsiteDataStoreDelegate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L63)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
