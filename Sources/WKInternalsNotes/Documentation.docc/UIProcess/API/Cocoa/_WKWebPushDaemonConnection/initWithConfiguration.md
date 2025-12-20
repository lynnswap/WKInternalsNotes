# ``WKInternalsNotes/_WKWebPushDaemonConnection/initWithConfiguration(_:)``

Web Push デーモン接続を構成して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithConfiguration:(_WKWebPushDaemonConnectionConfiguration *)configuration;
```

## Discussion
`WebPushDaemonConnectionConfiguration` を組み立て、`bundleIdentifierOverrideForTesting` と `partition` を設定する。`USE(EXTENSIONKIT)` が無効な場合は `hostApplicationAuditToken` をバイト配列に変換して `hostAppAuditTokenData` に設定する。最後に `machServiceName` と構成を用いて `API::WebPushDaemonConnection` を生成する。

## References
- [`_WKWebPushDaemonConnection.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L57)
- [`_WKWebPushDaemonConnection.mm#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L76)
- [`_WKWebPushDaemonConnection.mm#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L81)
- [`_WKWebPushDaemonConnection.mm#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L88)
- [`_WKWebPushDaemonConnection.mm#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L95)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
