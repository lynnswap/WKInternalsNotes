# ``WKInternalsNotes/_WKWebPushDaemonConnection/getNextPendingPushMessage(_:)``

保留中の Push メッセージを取得する。

## Objective-C Declaration
```objective-c
- (void)getNextPendingPushMessage:(void (^)(_WKWebPushMessage *))completionHandler;
```

## Discussion
`getNextPendingPushMessage` の結果が存在しない場合は `nil` を返し、存在する場合は `WebPushMessage` をラップして返す。

## References
- [`_WKWebPushDaemonConnection.h#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L65)
- [`_WKWebPushDaemonConnection.mm#L173`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L173)
- [`_WKWebPushDaemonConnection.mm#L175`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L175)
- [`_WKWebPushDaemonConnection.mm#L179`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L179)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
