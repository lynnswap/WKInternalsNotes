# ``WKInternalsNotes/_WKNotificationData/dir``

通知のテキスト方向を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKNotificationDirection dir;
```

## Default Value
`WebCore::NotificationData::direction` の値。

## Discussion
`WebCore::NotificationDirection` を `_WKNotificationDirection` に変換して返す。

## References
- [`_WKNotificationData.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L44)
- [`_WKNotificationData.mm#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L109)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
