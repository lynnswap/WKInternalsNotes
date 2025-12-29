# ``WKInternalsNotes/WKStylusDeviceObserver/hasStylusDevice``

スタイラス入力が期待されるかどうかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL hasStylusDevice;
```

## Default Value
`UIScribbleInteraction.isPencilInputExpected` の値。

## Discussion
内部 setter では値が変化したときに `WebProcessProxy::notifyHasStylusDeviceChanged` を通知し、タイマーを停止して状態を更新する。公開 API は読み取り専用。

## References
- [`WKStylusDeviceObserver.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKStylusDeviceObserver.h#L37)
- [`WKStylusDeviceObserver.mm#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKStylusDeviceObserver.mm#L72)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
