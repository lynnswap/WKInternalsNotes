# ``WKInternalsNotes/_WKWebPushDaemonConnection/cancelNotification(_:uuid:)``

通知の表示を取り消す。

## Objective-C Declaration
```objective-c
- (void)cancelNotification:(NSURL *)securityOriginURL uuid:(NSUUID *)notificationIdentifier;
```

## Discussion
`NSUUID` を `WTF::UUID` に変換して `cancelNotification` を呼び出す。実装コメントでは `notificationIdentifier` が `nil` の場合にのみ変換が失敗し、API の誤用になるとしている。

## References
- [`_WKWebPushDaemonConnection.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L68)
- [`_WKWebPushDaemonConnection.mm#L207`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L207)
- [`_WKWebPushDaemonConnection.mm#L209`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L209)
- [`_WKWebPushDaemonConnection.mm#L210`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L210)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
