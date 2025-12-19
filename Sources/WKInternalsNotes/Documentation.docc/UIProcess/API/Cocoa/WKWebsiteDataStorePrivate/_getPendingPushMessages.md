# ``WKInternalsNotes/WKWebsiteDataStore/_getPendingPushMessages(_:)``

保留中の Push メッセージ一覧を取得する。

## Objective-C Declaration
```objective-c
-(void)_getPendingPushMessages:(void(^)(NSArray<NSDictionary *> *))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`getPendingPushMessages` の結果を辞書配列に変換して `completionHandler` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L130`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L130)
- [`WKWebsiteDataStore.mm#L1283`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1283)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
