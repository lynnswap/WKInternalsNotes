# ``WKInternalsNotes/WKWebsiteDataStore/_setResourceLoadStatisticsTimeAdvanceForTesting(_:completionHandler:)``

テスト用にリソースロード統計の時間を進める。

## Objective-C Declaration
```objective-c
- (void)_setResourceLoadStatisticsTimeAdvanceForTesting:(NSTimeInterval)time completionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Discussion
`Seconds` に変換して `setResourceLoadStatisticsTimeAdvanceForTesting` を呼び、完了後に `completionHandler` を実行する。

## References
- [`WKWebsiteDataStorePrivate.h#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L73)
- [`WKWebsiteDataStore.mm#L960`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L960)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
