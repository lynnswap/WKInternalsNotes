# ``WKInternalsNotes/WKWebsiteDataStore/_sendNetworkProcessWillSuspendImminently()``

NetworkProcess のサスペンド直前を通知する。

## Objective-C Declaration
```objective-c
- (void)_sendNetworkProcessWillSuspendImminently WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`sendNetworkProcessWillSuspendImminentlyForTesting` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L117)
- [`WKWebsiteDataStore.mm#L1210`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1210)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
