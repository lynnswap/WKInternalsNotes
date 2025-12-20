# ``WKInternalsNotes/_WKWebPushDaemonConnection/subscribeToPushServiceForScope(_:applicationServerKey:completionHandler:)``

Push サービスへの購読を開始する。

## Objective-C Declaration
```objective-c
- (void)subscribeToPushServiceForScope:(NSURL *)scopeURL applicationServerKey:(NSData *)key completionHandler:(void (^)(_WKWebPushSubscriptionData *, NSError *))completionHandler;
```

## Discussion
`applicationServerKey` をバイト列に変換して `subscribeToPushService` を呼び出す。成功時は `WebPushSubscriptionData` をラップして返し、失敗時は `WKErrorDomain` と `WKErrorUnknown` を使った `NSError` を生成して返す。

## References
- [`_WKWebPushDaemonConnection.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L62)
- [`_WKWebPushDaemonConnection.mm#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L134)
- [`_WKWebPushDaemonConnection.mm#L136`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L136)
- [`_WKWebPushDaemonConnection.mm#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L141)
- [`_WKWebPushDaemonConnection.mm#L142`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L142)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
