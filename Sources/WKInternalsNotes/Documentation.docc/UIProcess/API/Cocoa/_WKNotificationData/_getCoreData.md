# ``WKInternalsNotes/_WKNotificationData/_getCoreData()``

内部の `NotificationData` を返す。

## Objective-C Declaration
```objective-c
-(const WebCore::NotificationData&)_getCoreData;
```

## Discussion
保持している `_coreData` を参照で返す。

## References
- [`_WKNotificationDataInternal.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationDataInternal.h#L36)
- [`_WKNotificationData.mm#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L79)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
