# ``WKInternalsNotes/WKWebsiteDataStore/_forceNetworkProcessToTaskSuspendForTesting()``

テスト用に `NetworkProcess` のタスクサスペンドを強制する。

## Objective-C Declaration
```objective-c
- (void)_forceNetworkProcessToTaskSuspendForTesting WK_API_AVAILABLE(macos(15.4), ios(18.4));
```

## Discussion
`networkProcessIfExists()` があれば throttler の `invalidateAllActivitiesAndDropAssertion()` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L120)
- [`WKWebsiteDataStore.mm#L1241`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1241)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
