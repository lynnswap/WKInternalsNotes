# ``WKInternalsNotes/_WKMutableNotificationData/tag``

`@dynamic` のためアクセサ実装は `_WKNotificationData` を利用する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, copy) NSString *tag;
```

## Default Value
`WebCore::NotificationData` の既定値に依存。

## Discussion
`_coreData.tag` に代入し、取得時は `createNSString()` で返す。

## References
- [`_WKNotificationData.h#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L71)
- [`_WKNotificationData.mm#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L141)
- [`_WKNotificationData.mm#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L146)
- [`_WKNotificationData.mm#L250`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L250)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
