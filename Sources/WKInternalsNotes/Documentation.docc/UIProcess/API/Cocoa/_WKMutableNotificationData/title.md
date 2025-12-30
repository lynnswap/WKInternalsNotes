# ``WKInternalsNotes/_WKMutableNotificationData/title``

`@dynamic` のためアクセサ実装は `_WKNotificationData` を利用する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, copy) NSString *title;
```

## Default Value
`WebCore::NotificationData` の既定値に依存。

## Discussion
`_coreData.title` に代入し、取得時は `createNSString()` で返す。

## References
- [`_WKNotificationData.h#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L67)
- [`_WKNotificationData.mm#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L84)
- [`_WKNotificationData.mm#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L89)
- [`_WKNotificationData.mm#L246`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L246)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
