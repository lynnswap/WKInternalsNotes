# ``WKInternalsNotes/_WKWebPushDaemonConnection/getSubscriptionForScope(_:completionHandler:)``

指定スコープの購読情報を取得する。

## Objective-C Declaration
```objective-c
- (void)getSubscriptionForScope:(NSURL *)scopeURL completionHandler:(void (^)(_WKWebPushSubscriptionData *, NSError *))completionHandler;
```

## Discussion
`getPushSubscription` の結果が成功で購読情報がある場合はラップして返す。成功だが購読が存在しない場合は `nil` を返す。失敗時は `WKErrorDomain` と `WKErrorUnknown` を使った `NSError` を生成して返す。

## References
- [`_WKWebPushDaemonConnection.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L64)
- [`_WKWebPushDaemonConnection.mm#L158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L158)
- [`_WKWebPushDaemonConnection.mm#L160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L160)
- [`_WKWebPushDaemonConnection.mm#L162`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L162)
- [`_WKWebPushDaemonConnection.mm#L168`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L168)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
