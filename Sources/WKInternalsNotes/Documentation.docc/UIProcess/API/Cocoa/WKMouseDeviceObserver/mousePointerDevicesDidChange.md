# ``WKInternalsNotes/WKMouseDeviceObserver/mousePointerDevicesDidChange(_:)``

マウス接続状態の変化を WebProcess に通知する。

## Objective-C Declaration
```objective-c
- (void)mousePointerDevicesDidChange:(BOOL)hasMouseDevice;
```

## Discussion
`WebKit::WebProcessProxy::notifyHasMouseDeviceChanged` を呼び、UIProcess から WebProcess へ状態を伝播する。

## References
- [WKMouseDeviceObserver.h#L49](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseDeviceObserver.h#L49)
- [WKMouseDeviceObserver.mm#L35](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseDeviceObserver.mm#L35)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
