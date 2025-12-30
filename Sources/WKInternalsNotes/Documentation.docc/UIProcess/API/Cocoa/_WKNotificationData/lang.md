# ``WKInternalsNotes/_WKNotificationData/lang``

通知の言語コードを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *lang;
```

## Default Value
`WebCore::NotificationData::language` の値。

## Discussion
内部の `_coreData.language` を `NSString` 化して返す。

## References
- [`_WKNotificationData.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L45)
- [`_WKNotificationData.mm#L126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L126)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
