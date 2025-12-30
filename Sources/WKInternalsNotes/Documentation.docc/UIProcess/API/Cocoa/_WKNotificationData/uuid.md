# ``WKInternalsNotes/_WKNotificationData/uuid``

通知 UUID を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSUUID *uuid;
```

## Default Value
`WebCore::NotificationData::notificationID` の UUID 変換結果。

## Discussion
`notificationID` を `NSUUID` に変換して返す。

## References
- [`_WKNotificationData.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L56)
- [`_WKNotificationData.mm#L220`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L220)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
