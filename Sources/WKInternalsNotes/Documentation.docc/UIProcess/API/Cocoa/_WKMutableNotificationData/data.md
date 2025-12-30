# ``WKInternalsNotes/_WKMutableNotificationData/data``

`@dynamic` のためアクセサ実装は `_WKNotificationData` を利用する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, copy) NSData *data;
```

## Default Value
`WebCore::NotificationData` の既定値に依存。

## Discussion
setter は `makeVector(data)` を用いて `_coreData.data` に格納し、getter は `toNSData(_coreData.data.span())` を返す。

## References
- [`_WKNotificationData.h#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L73)
- [`_WKNotificationData.mm#L173`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L173)
- [`_WKNotificationData.mm#L178`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L178)
- [`_WKNotificationData.mm#L252`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L252)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
