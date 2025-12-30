# ``WKInternalsNotes/_WKNotificationData/body``

通知本文を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *body;
```

## Default Value
`WebCore::NotificationData::body` の値。

## Discussion
内部の `_coreData.body` を `NSString` 化して返す。

## References
- [`_WKNotificationData.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L46)
- [`_WKNotificationData.mm#L136`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L136)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
