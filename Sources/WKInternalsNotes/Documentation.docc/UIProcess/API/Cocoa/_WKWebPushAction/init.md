# ``WKInternalsNotes/_WKWebPushAction/init()``

公開初期化子としては使用できない。

## Objective-C Declaration
```objective-c
- (instancetype)init NS_UNAVAILABLE;
```

## Discussion
`NS_UNAVAILABLE` で公開初期化子を禁止しているため、外部からは `webPushActionWithDictionary:` または `_webPushActionWithNotificationResponse:` を使用する。

## References
- [`_WKWebPushAction.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushAction.h#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
