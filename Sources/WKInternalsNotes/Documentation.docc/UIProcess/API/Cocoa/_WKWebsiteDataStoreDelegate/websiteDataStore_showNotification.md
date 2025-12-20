# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/websiteDataStore(_:showNotification:)``

通知を表示する。

## Objective-C Declaration
```objective-c
- (void)websiteDataStore:(WKWebsiteDataStore *)dataStore showNotification:(_WKNotificationData *)notificationData;
```

## Discussion
WebKit 側の showNotification 実装では、delegate または `dataStore` が未設定の場合は `false` を返す。`NotificationData` から `_WKNotificationData` を生成して delegate に渡し、呼び出しに成功した場合は `true` を返す。

## References
- [`_WKWebsiteDataStoreDelegate.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L66)
- [`WKWebsiteDataStore.mm#L207`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L207)
- [`WKWebsiteDataStore.mm#L213`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L213)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
