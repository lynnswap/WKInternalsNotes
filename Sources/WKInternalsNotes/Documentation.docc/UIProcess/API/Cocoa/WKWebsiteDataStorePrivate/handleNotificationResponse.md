# ``WKInternalsNotes/WKWebsiteDataStore/handleNotificationResponse(_:)``

通知レスポンスを処理する。

## Objective-C Declaration
```objective-c
+ (BOOL)handleNotificationResponse:(UNNotificationResponse *)response WK_API_AVAILABLE(ios(18.2));
```

## Discussion
iOS では `_WKWebsiteDataStoreBSActionHandler` に委譲し、他プラットフォームでは `NO` を返す。

## References
- [`WKWebsiteDataStorePrivate.h#L155`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L155)
- [`WKWebsiteDataStore.mm#L387`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L387)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
