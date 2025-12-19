# ``WKInternalsNotes/WKWebsiteDataStore/_makeNextNetworkProcessLaunchFailForTesting()``

次回の `NetworkProcess` 起動をテスト用に失敗させる。

## Objective-C Declaration
```objective-c
+ (void)_makeNextNetworkProcessLaunchFailForTesting WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`WebsiteDataStore::makeNextNetworkProcessLaunchFailForTesting()` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L123)
- [`WKWebsiteDataStore.mm#L1231`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1231)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
