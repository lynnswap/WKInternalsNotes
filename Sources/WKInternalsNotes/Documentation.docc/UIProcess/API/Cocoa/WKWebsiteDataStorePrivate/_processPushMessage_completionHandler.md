# ``WKInternalsNotes/WKWebsiteDataStore/_processPushMessage(_:completionHandler:)``

Push メッセージを処理する。

## Objective-C Declaration
```objective-c
-(void)_processPushMessage:(NSDictionary *)pushMessage completionHandler:(void(^)(bool))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
辞書から `WebPushMessage` を復元し、失敗時は `false` を返す。成功時は `processPushMessage` の結果を `completionHandler` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L131`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L131)
- [`WKWebsiteDataStore.mm#L1297`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1297)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
