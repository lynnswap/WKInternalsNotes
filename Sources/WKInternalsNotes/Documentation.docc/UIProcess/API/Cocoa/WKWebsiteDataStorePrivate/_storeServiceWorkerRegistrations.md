# ``WKInternalsNotes/WKWebsiteDataStore/_storeServiceWorkerRegistrations(_:)``

Service Worker 登録を保存する。

## Objective-C Declaration
```objective-c
-(void)_storeServiceWorkerRegistrations:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
`storeServiceWorkerRegistrations` を呼び、完了後に `completionHandler` を実行する。

## References
- [`WKWebsiteDataStorePrivate.h#L145`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L145)
- [`WKWebsiteDataStore.mm#L1428`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1428)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
