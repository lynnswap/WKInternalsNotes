# ``WKInternalsNotes/_WKWebPushDaemonConnection/showNotification(_:completionHandler:)``

通知を表示する。

## Objective-C Declaration
```objective-c
- (void)showNotification:(_WKNotificationData *)notificationData completionHandler:(void (^)(void))completionHandler;
```

## Discussion
`_WKNotificationData` から Core データを取り出して `showNotification` を呼び出し、完了時に `completionHandler` を実行する。

## References
- [`_WKWebPushDaemonConnection.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L66)
- [`_WKWebPushDaemonConnection.mm#L184`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L184)
- [`_WKWebPushDaemonConnection.mm#L186`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L186)
- [`_WKWebPushDaemonConnection.mm#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
