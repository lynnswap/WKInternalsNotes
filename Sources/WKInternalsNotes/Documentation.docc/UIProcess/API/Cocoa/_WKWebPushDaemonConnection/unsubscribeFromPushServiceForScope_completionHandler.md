# ``WKInternalsNotes/_WKWebPushDaemonConnection/unsubscribeFromPushServiceForScope(_:completionHandler:)``

Push サービスからの購読解除を行う。

## Objective-C Declaration
```objective-c
- (void)unsubscribeFromPushServiceForScope:(NSURL *)scopeURL completionHandler:(void (^)(BOOL unsubscribed, NSError *))completionHandler;
```

## Discussion
`unsubscribeFromPushService` の結果を受け取り、成功時は `unsubscribed` を返す。失敗時は `WKErrorDomain` と `WKErrorUnknown` を使った `NSError` を生成して返し、`unsubscribed` を `NO` にする。

## References
- [`_WKWebPushDaemonConnection.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L63)
- [`_WKWebPushDaemonConnection.mm#L147`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L147)
- [`_WKWebPushDaemonConnection.mm#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L149)
- [`_WKWebPushDaemonConnection.mm#L153`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L153)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
