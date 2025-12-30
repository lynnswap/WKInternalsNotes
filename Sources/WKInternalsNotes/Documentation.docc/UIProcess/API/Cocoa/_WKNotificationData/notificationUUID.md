# ``WKInternalsNotes/_WKNotificationData/notificationUUID``

内部の readwrite UUID プロパティ。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite) NSUUID *notificationUUID;
```

## Default Value
自動合成されるため初期値は `nil`。

## Discussion
クラス拡張で宣言されているが、明示的な getter/setter 実装は無い。

## References
- [`_WKNotificationData.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKNotificationData.mm#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
