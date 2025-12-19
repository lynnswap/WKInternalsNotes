# ``WKInternalsNotes/WKWebsiteDataStore/_runningOrTerminatingServiceWorkerCountForTesting(_:)``

テスト用に実行中/終了処理中の Service Worker 数を取得する。

## Objective-C Declaration
```objective-c
- (void)_runningOrTerminatingServiceWorkerCountForTesting:(void(^)(NSUInteger))completionHandler WK_API_AVAILABLE(macos(15.4), ios(18.4));
```

## Discussion
`runningOrTerminatingServiceWorkerCountForTesting` を呼び、結果を `completionHandler` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L157`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L157)
- [`WKWebsiteDataStore.mm#L1583`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1583)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
