# ``WKInternalsNotes/_WKNotificationData/origin``

origin 文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *origin;
```

## Default Value
`WebCore::NotificationData::originString` の値。

## Discussion
内部の `_coreData.originString` を `NSString` 化して返す。

## References
- [`_WKNotificationData.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L51)
- [`_WKNotificationData.mm#L183`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L183)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
