# ``WKInternalsNotes/_WKWebPushAction/coreNotificationData``

通知応答から復元した `NotificationData` を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) std::optional<WebCore::NotificationData> coreNotificationData;
```

## Default Value
空 (`std::nullopt`)。

## Discussion
内部で読み書き可能なプロパティ。`_webPushActionWithNotificationResponse:` が `NotificationData::fromDictionary` で復元した値を設定する。辞書から生成する経路では設定されない。

## References
- [`_WKWebPushActionInternal.h#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushActionInternal.h#L31)
- [`_WKWebPushAction.mm#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushAction.mm#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
