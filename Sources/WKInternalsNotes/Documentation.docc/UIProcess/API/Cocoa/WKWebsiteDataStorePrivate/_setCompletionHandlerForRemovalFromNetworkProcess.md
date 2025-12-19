# ``WKInternalsNotes/WKWebsiteDataStore/_setCompletionHandlerForRemovalFromNetworkProcess(_:)``

NetworkProcess からの削除完了ハンドラを設定する。

## Objective-C Declaration
```objective-c
-(void)_setCompletionHandlerForRemovalFromNetworkProcess:(void(^)(NSError* error))completionHandler WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
エラーメッセージがある場合は `NSError` に変換して `completionHandler` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L146)
- [`WKWebsiteDataStore.mm#L1487`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1487)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
