# ``WKInternalsNotes/_WKMutableNotificationData/lang``

`@dynamic` のためアクセサ実装は `_WKNotificationData` を利用する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, copy) NSString *lang;
```

## Default Value
`WebCore::NotificationData` の既定値に依存。

## Discussion
`_coreData.language` に代入し、取得時は `createNSString()` で返す。

## References
- [`_WKNotificationData.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L69)
- [`_WKNotificationData.mm#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L121)
- [`_WKNotificationData.mm#L126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L126)
- [`_WKNotificationData.mm#L248`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L248)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
