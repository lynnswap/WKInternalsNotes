# ``WKInternalsNotes/WKStylusDeviceObserver/sharedInstance()``

スタイラス監視のシングルトンを返す。

## Objective-C Declaration
```objective-c
+ (WKStylusDeviceObserver *)sharedInstance;
```

## Discussion
`NeverDestroyed` の静的インスタンスを `adoptNS` で保持して返す。

## References
- [`WKStylusDeviceObserver.h#L30`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKStylusDeviceObserver.h#L30)
- [`WKStylusDeviceObserver.mm#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKStylusDeviceObserver.mm#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
