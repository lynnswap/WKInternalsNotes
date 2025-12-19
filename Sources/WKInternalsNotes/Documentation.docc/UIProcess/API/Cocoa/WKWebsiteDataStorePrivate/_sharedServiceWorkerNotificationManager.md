# ``WKInternalsNotes/WKWebsiteDataStore/_sharedServiceWorkerNotificationManager()``

Service Worker 用の共有通知マネージャを取得する。

## Objective-C Declaration
```objective-c
+ (WKNotificationManagerRef)_sharedServiceWorkerNotificationManager WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`WebNotificationManagerProxy::serviceWorkerManagerSingleton()` を返す。

## References
- [`WKWebsiteDataStorePrivate.h#L113`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L113)
- [`WKWebsiteDataStore.mm#L1150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1150)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
