# ``WKInternalsNotes/_WKWebPushDaemonConnectionConfiguration/partition``

パーティション名（nullable）を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, nullable) NSString *partition;
```

## Default Value
`init` では設定されず `nil`。

## Discussion
`initWithConfiguration:` で `WebPushDaemonConnectionConfiguration` に渡され、接続先の partition として使われる。

## References
- [`_WKWebPushDaemonConnection.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L47)
- [`_WKWebPushDaemonConnection.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L66)
- [`_WKWebPushDaemonConnection.mm#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L84)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
