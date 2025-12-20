# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/websiteDataStore(_:domain:didExceedMemoryFootprintThreshold:withPageCount:processLifetime:inForeground:wasPrivateRelayed:canSuspend:)``

メモリフットプリントの閾値超過を通知する。

## Objective-C Declaration
```objective-c
- (void)websiteDataStore:(WKWebsiteDataStore *)dataStore domain:(NSString *)registrableDomain didExceedMemoryFootprintThreshold:(size_t)footprint withPageCount:(NSUInteger)pageCount processLifetime:(NSTimeInterval)processLifetime inForeground:(BOOL)inForeground wasPrivateRelayed:(BOOL)wasPrivateRelayed canSuspend:(BOOL)canSuspend;
```

## Discussion
delegate が未実装の場合は呼ばれない。`processLifetime` は秒に変換し、`wasPrivateRelayed` と `canSuspend` は内部列挙から `BOOL` に変換して渡す。

## References
- [`_WKWebsiteDataStoreDelegate.h#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L74)
- [`WKWebsiteDataStore.mm#L354`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L354)
- [`WKWebsiteDataStore.mm#L359`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L359)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
