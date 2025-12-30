# ``WKInternalsNotes/_WKNotificationData/userInfo``

通知データの辞書表現を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSDictionary *userInfo;
```

## Default Value
`WebCore::NotificationData::dictionaryRepresentation()` の値。

## Discussion
`_coreData.dictionaryRepresentation()` を返す。

## References
- [`_WKNotificationData.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L57)
- [`_WKNotificationData.mm#L225`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L225)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
