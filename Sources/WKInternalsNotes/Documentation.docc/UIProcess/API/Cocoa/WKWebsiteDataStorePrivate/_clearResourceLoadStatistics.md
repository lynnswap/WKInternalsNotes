# ``WKInternalsNotes/WKWebsiteDataStore/_clearResourceLoadStatistics(_:)``

リソースロード統計をクリアする。

## Objective-C Declaration
```objective-c
- (void)_clearResourceLoadStatistics:(void (^)(void))completionHandler WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
`scheduleClearInMemoryAndPersistent(ShouldGrandfatherStatistics::No)` を呼び、完了後に `completionHandler` を実行する。

## References
- [`WKWebsiteDataStorePrivate.h#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L87)
- [`WKWebsiteDataStore.mm#L1035`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1035)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
