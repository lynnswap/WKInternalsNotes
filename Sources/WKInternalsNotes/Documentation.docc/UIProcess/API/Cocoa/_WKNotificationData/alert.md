# ``WKInternalsNotes/_WKNotificationData/alert``

通知アラート設定を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKNotificationAlert alert;
```

## Default Value
`WebCore::NotificationData::silent` の状態に対応する値。

## Discussion
`silent` が `std::nullopt` なら `Default`、`true` なら `Silent`、`false` なら `Enabled` を返す。

## References
- [`_WKNotificationData.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L48)
- [`_WKNotificationData.mm#L166`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L166)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
