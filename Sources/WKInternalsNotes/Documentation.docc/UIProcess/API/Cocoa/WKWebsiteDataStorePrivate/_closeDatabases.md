# ``WKInternalsNotes/WKWebsiteDataStore/_closeDatabases(_:)``

データベースを閉じる。

## Objective-C Declaration
```objective-c
- (void)_closeDatabases:(void (^)(void))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`closeDatabases` を呼び、完了後に `completionHandler` を実行する。

## References
- [`WKWebsiteDataStorePrivate.h#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L88)
- [`WKWebsiteDataStore.mm#L1042`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1042)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
