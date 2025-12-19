# ``WKInternalsNotes/WKWebsiteDataStore/_setCachedProcessSuspensionDelayForTesting(_:)``

テスト用にキャッシュプロセスのサスペンド遅延を設定する。

## Objective-C Declaration
```objective-c
+ (void)_setCachedProcessSuspensionDelayForTesting:(double)delayInSeconds WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`WebsiteDataStore::setCachedProcessSuspensionDelayForTesting` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L97)
- [`WKWebsiteDataStore.mm#L1058`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1058)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
