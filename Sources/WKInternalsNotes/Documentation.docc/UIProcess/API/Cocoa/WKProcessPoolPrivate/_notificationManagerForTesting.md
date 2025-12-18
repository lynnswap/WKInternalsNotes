# ``WKInternalsNotes/WKProcessPool/_notificationManagerForTesting()``

通知マネージャの API 参照を返す（テスト用）。

## Objective-C Declaration
```objective-c
- (WKNotificationManagerRef)_notificationManagerForTesting;
```

## Discussion
`WebNotificationManagerProxy` の supplement を取得し、`WebKit::toAPI` で `WKNotificationManagerRef` に変換して返す。

## References
- [`WKProcessPoolPrivate.h#L183`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L183)
- [`WKProcessPool.mm#L680`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L680)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
