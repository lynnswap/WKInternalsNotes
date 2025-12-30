# ``WKInternalsNotes/_WKMutableNotificationData/dir``

`@dynamic` のためアクセサ実装は `_WKNotificationData` を利用する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite) _WKNotificationDirection dir;
```

## Default Value
`WebCore::NotificationData` の既定値に依存。

## Discussion
setter で `_WKNotificationDirection` を `WebCore::NotificationDirection` に変換し、getter で逆変換する。

## References
- [`_WKNotificationData.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L68)
- [`_WKNotificationData.mm#L94`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L94)
- [`_WKNotificationData.mm#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L109)
- [`_WKNotificationData.mm#L247`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L247)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
