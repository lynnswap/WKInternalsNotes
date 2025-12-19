# ``WKInternalsNotes/_WKWebPushDaemonConnectionConfiguration/hostApplicationAuditToken``

ホストアプリの audit token を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, assign) audit_token_t hostApplicationAuditToken;
```

## Default Value
`init` では設定されず、呼び出し元が値を設定する。

## Discussion
`USE(EXTENSIONKIT)` でない場合に `initWithConfiguration:` が audit token をバイト列へ変換し、接続設定に渡す。

## References
- [`_WKWebPushDaemonConnection.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L48)
- [`_WKWebPushDaemonConnection.mm#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L88)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
