# ``WKInternalsNotes/_WKNotificationData/title``

通知タイトルを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *title;
```

## Default Value
`WebCore::NotificationData::title` の値。

## Discussion
内部の `_coreData.title` を `NSString` 化して返す。

## References
- [`_WKNotificationData.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L43)
- [`_WKNotificationData.mm#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L89)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
