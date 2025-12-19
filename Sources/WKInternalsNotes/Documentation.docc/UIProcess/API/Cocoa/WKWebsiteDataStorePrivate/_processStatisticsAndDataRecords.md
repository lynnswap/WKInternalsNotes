# ``WKInternalsNotes/WKWebsiteDataStore/_processStatisticsAndDataRecords(_:)``

統計とデータレコードの処理をスケジュールする。

## Objective-C Declaration
```objective-c
- (void)_processStatisticsAndDataRecords:(void (^)(void))completionHandler WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
`scheduleStatisticsAndDataRecordsProcessing` を呼び、完了後に `completionHandler` を実行する。

## References
- [`WKWebsiteDataStorePrivate.h#L93`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L93)
- [`WKWebsiteDataStore.mm#L1084`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1084)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
