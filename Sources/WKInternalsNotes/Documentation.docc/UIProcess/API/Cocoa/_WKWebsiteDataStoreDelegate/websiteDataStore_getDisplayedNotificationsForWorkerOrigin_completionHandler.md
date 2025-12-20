# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/websiteDataStore(_:getDisplayedNotificationsForWorkerOrigin:completionHandler:)``

表示中の通知一覧を取得する。

## Objective-C Declaration
```objective-c
- (void)websiteDataStore:(WKWebsiteDataStore *)dataStore getDisplayedNotificationsForWorkerOrigin:(WKSecurityOrigin *)workerOrigin completionHandler:(void (^)(NSArray<NSDictionary *> *))completionHandler;
```

## Discussion
delegate または `dataStore` が未設定の場合は空配列で完了する。受け取った辞書配列は `NotificationData::fromDictionary` で変換され、無効な辞書は `RELEASE_ASSERT` で検出される。

## References
- [`_WKWebsiteDataStoreDelegate.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L68)
- [`WKWebsiteDataStore.mm#L242`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L242)
- [`WKWebsiteDataStore.mm#L254`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L254)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
