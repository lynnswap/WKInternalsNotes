# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/websiteDataStore(_:reportServiceWorkerConsoleMessage:)``

Service Worker の console メッセージを通知する。

## Objective-C Declaration
```objective-c
- (void)websiteDataStore:(WKWebsiteDataStore *)dataStore reportServiceWorkerConsoleMessage:(NSString *)message;
```

## Discussion
delegate が `reportServiceWorkerConsoleMessage:` を実装している場合のみ呼ばれる。実装が無い場合は何もしない。

## References
- [`_WKWebsiteDataStoreDelegate.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L64)
- [`WKWebsiteDataStore.mm#L200`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L200)
- [`WKWebsiteDataStore.mm#L204`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L204)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
