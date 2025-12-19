# ``WKInternalsNotes/WKWebsiteDataStore/_sendNetworkProcessDidResume()``

NetworkProcess の再開を通知する。

## Objective-C Declaration
```objective-c
- (void)_sendNetworkProcessDidResume WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`sendNetworkProcessDidResume` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L118`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L118)
- [`WKWebsiteDataStore.mm#L1216`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1216)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
