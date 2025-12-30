# ``WKInternalsNotes/_WKMutableNotificationData/body``

`@dynamic` のためアクセサ実装は `_WKNotificationData` を利用する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, copy) NSString *body;
```

## Default Value
`WebCore::NotificationData` の既定値に依存。

## Discussion
`_coreData.body` に代入し、取得時は `createNSString()` で返す。

## References
- [`_WKNotificationData.h#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L70)
- [`_WKNotificationData.mm#L131`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L131)
- [`_WKNotificationData.mm#L136`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L136)
- [`_WKNotificationData.mm#L249`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L249)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
