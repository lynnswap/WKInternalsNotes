# ``WKInternalsNotes/_WKMutableNotificationData/init()``

`_WKNotificationData` の `_init` を呼んで初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)init;
```

## Discussion
`[super _init]` が失敗した場合は `nil` を返し、成功時は `self` を返す。

## References
- [`_WKNotificationData.h#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.h#L65)
- [`_WKNotificationData.mm#L257`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L257)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
