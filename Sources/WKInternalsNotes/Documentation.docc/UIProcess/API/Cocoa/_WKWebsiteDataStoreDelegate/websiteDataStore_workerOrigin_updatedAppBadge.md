# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/websiteDataStore(_:workerOrigin:updatedAppBadge:)``

Service Worker の app badge 更新を通知する。

## Objective-C Declaration
```objective-c
- (void)websiteDataStore:(WKWebsiteDataStore *)dataStore workerOrigin:(WKSecurityOrigin *)workerOrigin updatedAppBadge:(NSNumber *)badge;
```

## Discussion
delegate または `dataStore` が未設定の場合は呼ばれない。`badge` が `nil` の場合はクリア扱いで、そのまま `nil` を渡す。

## References
- [`_WKWebsiteDataStoreDelegate.h#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L67)
- [`WKWebsiteDataStore.mm#L263`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L263)
- [`WKWebsiteDataStore.mm#L273`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L273)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
