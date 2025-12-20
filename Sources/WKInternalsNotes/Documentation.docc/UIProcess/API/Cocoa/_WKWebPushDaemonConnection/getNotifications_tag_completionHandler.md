# ``WKInternalsNotes/_WKWebPushDaemonConnection/getNotifications(_:tag:completionHandler:)``

通知一覧を取得する。

## Objective-C Declaration
```objective-c
- (void)getNotifications:(NSURL *)scopeURL tag:(NSString *)tag completionHandler:(void (^)(NSArray<_WKNotificationData *> *, NSError *))completionHandler;
```

## Discussion
`getNotifications` の成功時は `WebPushNotificationData` を `_WKNotificationData` に変換して配列を返す。失敗時は `WKErrorDomain` と `WKErrorUnknown` を使った `NSError` を生成して返す。

## References
- [`_WKWebPushDaemonConnection.h#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L67)
- [`_WKWebPushDaemonConnection.mm#L191`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L191)
- [`_WKWebPushDaemonConnection.mm#L193`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L193)
- [`_WKWebPushDaemonConnection.mm#L195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L195)
- [`_WKWebPushDaemonConnection.mm#L202`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L202)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
