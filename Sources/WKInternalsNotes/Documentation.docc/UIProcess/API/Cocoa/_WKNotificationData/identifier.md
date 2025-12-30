# ``WKInternalsNotes/_WKNotificationData/identifier``

通知識別子を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *identifier;
```

## Default Value
`WebCore::NotificationData::notificationID` の文字列表現。

## Discussion
`notificationID.toString()` を `NSString` 化して返す。

## References
- [`_WKNotificationData.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L55)
- [`_WKNotificationData.mm#L208`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L208)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
