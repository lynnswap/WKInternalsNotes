# ``WKInternalsNotes/_WKNotificationData/serviceWorkerRegistrationURL``

Service Worker 登録 URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURL *serviceWorkerRegistrationURL;
```

## Default Value
`WebCore::NotificationData::serviceWorkerRegistrationURL` の値。

## Discussion
内部の `_coreData.serviceWorkerRegistrationURL` を `NSURL` 化して返す。

## References
- [`_WKNotificationData.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L53)
- [`_WKNotificationData.mm#L203`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L203)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
