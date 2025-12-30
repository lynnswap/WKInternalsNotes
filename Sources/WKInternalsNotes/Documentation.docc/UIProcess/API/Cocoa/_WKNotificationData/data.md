# ``WKInternalsNotes/_WKNotificationData/data``

通知に紐づくデータを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSData *data;
```

## Default Value
`WebCore::NotificationData::data` の値。

## Discussion
内部の `_coreData.data` を `NSData` に変換して返す。

## References
- [`_WKNotificationData.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L49)
- [`_WKNotificationData.mm#L178`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L178)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
