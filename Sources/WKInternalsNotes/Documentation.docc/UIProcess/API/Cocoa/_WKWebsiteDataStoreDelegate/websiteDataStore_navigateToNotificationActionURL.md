# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/websiteDataStore(_:navigateToNotificationActionURL:)``

通知アクションの遷移 URL を通知する。

## Objective-C Declaration
```objective-c
- (void)websiteDataStore:(WKWebsiteDataStore *)dataStore navigateToNotificationActionURL:(NSURL *)url;
```

## Discussion
delegate または `dataStore` が未設定の場合は呼ばれない。`url` を `NSURL` に変換してそのまま渡す。

## References
- [`_WKWebsiteDataStoreDelegate.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L69)
- [`WKWebsiteDataStore.mm#L276`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L276)
- [`WKWebsiteDataStore.mm#L281`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L281)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
