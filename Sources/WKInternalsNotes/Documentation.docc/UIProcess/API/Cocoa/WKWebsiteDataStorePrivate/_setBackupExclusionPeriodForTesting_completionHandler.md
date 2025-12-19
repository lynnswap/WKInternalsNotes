# ``WKInternalsNotes/WKWebsiteDataStore/_setBackupExclusionPeriodForTesting(_:completionHandler:)``

テスト用にバックアップ除外期間を設定する。

## Objective-C Declaration
```objective-c
-(void)_setBackupExclusionPeriodForTesting:(double)seconds completionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
iOS ファミリでは `setBackupExclusionPeriodForTesting` を呼び、その他では no-op で `completionHandler` を実行する。

## References
- [`WKWebsiteDataStorePrivate.h#L137`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L137)
- [`WKWebsiteDataStore.mm#L1461`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1461)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
