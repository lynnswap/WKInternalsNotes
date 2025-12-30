# ``WKInternalsNotes/_WKMutableNotificationData/securityOrigin``

`@dynamic` のためアクセサ実装は `_WKNotificationData` を利用する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, copy) NSURL *securityOrigin;
```

## Default Value
`WebCore::NotificationData` の既定値に依存。

## Discussion
setter は `WebCore::SecurityOriginData::fromURL(...)` の結果を `_coreData.originString` に保存し、getter は `originString` から `NSURL` を生成する。

## References
- [`_WKNotificationData.h#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L74)
- [`_WKNotificationData.mm#L188`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L188)
- [`_WKNotificationData.mm#L193`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L193)
- [`_WKNotificationData.mm#L253`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L253)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
