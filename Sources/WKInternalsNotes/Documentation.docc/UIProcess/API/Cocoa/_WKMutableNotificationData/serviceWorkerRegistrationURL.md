# ``WKInternalsNotes/_WKMutableNotificationData/serviceWorkerRegistrationURL``

`@dynamic` のためアクセサ実装は `_WKNotificationData` を利用する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, copy) NSURL *serviceWorkerRegistrationURL;
```

## Default Value
`WebCore::NotificationData` の既定値に依存。

## Discussion
`_coreData.serviceWorkerRegistrationURL` に保存し、取得時は `createNSURL()` で返す。

## References
- [`_WKNotificationData.h#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L75)
- [`_WKNotificationData.mm#L198`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L198)
- [`_WKNotificationData.mm#L203`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L203)
- [`_WKNotificationData.mm#L254`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L254)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
