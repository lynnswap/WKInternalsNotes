# ``WKInternalsNotes/_WKMutableNotificationData/uuid``

`@dynamic` のためアクセサ実装は `_WKNotificationData` を利用する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, copy) NSUUID *uuid;
```

## Default Value
`WebCore::NotificationData` の既定値に依存。

## Discussion
setter は `WTF::UUID::fromNSUUID` の結果が有効な場合に `_coreData.notificationID` を更新し、getter は `createNSUUID()` を返す。

## References
- [`_WKNotificationData.h#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L76)
- [`_WKNotificationData.mm#L213`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L213)
- [`_WKNotificationData.mm#L220`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L220)
- [`_WKNotificationData.mm#L255`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L255)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
