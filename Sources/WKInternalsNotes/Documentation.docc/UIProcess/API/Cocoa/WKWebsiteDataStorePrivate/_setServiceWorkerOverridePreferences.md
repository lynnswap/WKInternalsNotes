# ``WKInternalsNotes/WKWebsiteDataStore/_setServiceWorkerOverridePreferences(_:)``

Service Worker の上書き設定を指定する。

## Objective-C Declaration
```objective-c
-(void)_setServiceWorkerOverridePreferences:(WKPreferences *)preferences WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Discussion
`WKPreferences` の内部ポインタを渡し、`nil` の場合は解除する。

## References
- [`WKWebsiteDataStorePrivate.h#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L134)
- [`WKWebsiteDataStore.mm#L1435`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1435)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
