# ``WKInternalsNotes/WKWebsiteDataStore/_getPendingPushMessage(_:)``

保留中の Push メッセージを1件取得する。

## Objective-C Declaration
```objective-c
-(void)_getPendingPushMessage:(void(^)(NSDictionary *))completionHandler WK_API_AVAILABLE(macos(15.2), ios(18.2));
```

## Discussion
`getPendingPushMessage` の結果を辞書に変換して `completionHandler` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L129)
- [`WKWebsiteDataStore.mm#L1269`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1269)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
