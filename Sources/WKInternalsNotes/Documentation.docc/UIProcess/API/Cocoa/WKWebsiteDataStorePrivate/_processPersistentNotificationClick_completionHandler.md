# ``WKInternalsNotes/WKWebsiteDataStore/_processPersistentNotificationClick(_:completionHandler:)``

永続通知のクリックを処理する。

## Objective-C Declaration
```objective-c
-(void)_processPersistentNotificationClick:(NSDictionary *)notificationDictionaryRepresentation completionHandler:(void(^)(bool))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
辞書から `NotificationData` を復元し、失敗時は `false` を返す。成功時は `_processWebCorePersistentNotificationClick` に委譲する。

## References
- [`WKWebsiteDataStorePrivate.h#L132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L132)
- [`WKWebsiteDataStore.mm#L1335`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1335)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
