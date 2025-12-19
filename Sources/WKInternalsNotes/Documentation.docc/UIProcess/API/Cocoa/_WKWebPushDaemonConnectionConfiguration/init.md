# ``WKInternalsNotes/_WKWebPushDaemonConnectionConfiguration/init()``

デフォルトの webpushd 接続設定を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)init;
```

## Discussion
`ENABLE(RELOCATABLE_WEBPUSHD)` に応じて `machServiceName` を `com.apple.webkit.webpushd.relocatable.service` または `com.apple.webkit.webpushd.service` に設定する。

## References
- [`_WKWebPushDaemonConnection.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L45)
- [`_WKWebPushDaemonConnection.mm#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
