# ``WKInternalsNotes/WKContentView/_simulateLongPressActionAtLocation(_:)``

指定位置のロングプレスアクションをシミュレートする。

## Objective-C Declaration
```objective-c
- (void)_simulateLongPressActionAtLocation:(CGPoint)location;
```

## Discussion
位置情報更新後に `_actionForLongPress` を取得し、該当アクションがあれば `performSelector:` で実行する。

## References
- [`WKContentViewInteraction.h#L1031`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1031)
- [`WKContentViewInteraction.mm#L14484`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14484)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
