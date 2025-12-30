# ``WKInternalsNotes/_WKNotificationData/securityOrigin``

通知のセキュリティオリジンを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURL *securityOrigin;
```

## Default Value
`WebCore::NotificationData::originString` から生成された URL。

## Discussion
setter は `SecurityOriginData::fromURL` で `originString` を更新し、getter は `originString` から `NSURL` を生成して返す。

## References
- [`_WKNotificationData.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L52)
- [`_WKNotificationData.mm#L188`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L188)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
