# ``WKInternalsNotes/_WKMutableNotificationData/alert``

`@dynamic` のためアクセサ実装は `_WKNotificationData` を利用する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite) _WKNotificationAlert alert;
```

## Default Value
`_coreData.silent` が `std::nullopt` の場合は `_WKNotificationAlertDefault`。

## Discussion
setter は `alert` に応じて `_coreData.silent` を `std::nullopt`/`true`/`false` に設定し、getter は逆変換する。

## References
- [`_WKNotificationData.h#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L72)
- [`_WKNotificationData.mm#L151`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L151)
- [`_WKNotificationData.mm#L166`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L166)
- [`_WKNotificationData.mm#L251`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L251)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
