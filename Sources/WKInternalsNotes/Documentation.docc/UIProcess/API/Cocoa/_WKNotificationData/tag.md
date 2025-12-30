# ``WKInternalsNotes/_WKNotificationData/tag``

通知タグを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *tag;
```

## Default Value
`WebCore::NotificationData::tag` の値。

## Discussion
内部の `_coreData.tag` を `NSString` 化して返す。

## References
- [`_WKNotificationData.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L47)
- [`_WKNotificationData.mm#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L146)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
