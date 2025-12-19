# ``WKInternalsNotes/_WKWebPushDaemonConnectionConfiguration/machServiceName``

webpushd の Mach サービス名を指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSString *machServiceName;
```

## Default Value
`init` で `ENABLE(RELOCATABLE_WEBPUSHD)` の有無に応じて既定値が設定される。

## Discussion
既定値は `com.apple.webkit.webpushd.relocatable.service` または `com.apple.webkit.webpushd.service`。`dealloc` では `nil` にクリアされる。

## References
- [`_WKWebPushDaemonConnection.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L46)
- [`_WKWebPushDaemonConnection.mm#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L53)
- [`_WKWebPushDaemonConnection.mm#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L61)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
