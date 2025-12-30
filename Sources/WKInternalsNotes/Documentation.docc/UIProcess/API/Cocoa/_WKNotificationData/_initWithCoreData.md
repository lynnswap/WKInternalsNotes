# ``WKInternalsNotes/_WKNotificationData/_initWithCoreData(_:)``

内部の `NotificationData` を初期化して保持する。

## Objective-C Declaration
```objective-c
-(instancetype)_initWithCoreData:(const WebCore::NotificationData&)coreData;
```

## Discussion
`coreData` を `_coreData` にコピーして返す。

## References
- [`_WKNotificationDataInternal.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationDataInternal.h#L35)
- [`_WKNotificationData.mm#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L69)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
