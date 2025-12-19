# ``WKInternalsNotes/WKWebsiteDataStore/_sendNetworkProcessPrepareToSuspend(_:)``

NetworkProcess のサスペンド準備を通知する。

## Objective-C Declaration
```objective-c
- (void)_sendNetworkProcessPrepareToSuspend:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`sendNetworkProcessPrepareToSuspendForTesting` を呼び、完了後に `completionHandler` を実行する。

## References
- [`WKWebsiteDataStorePrivate.h#L116`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L116)
- [`WKWebsiteDataStore.mm#L1203`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1203)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
