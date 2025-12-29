# ``WKInternalsNotes/WKStylusDeviceObserver/init()``

公開初期化子としては使用できない。

## Objective-C Declaration
```objective-c
- (instancetype)init NS_UNAVAILABLE;
```

## Discussion
公開 API では `NS_UNAVAILABLE`。内部初期化では `UIScribbleInteraction.isPencilInputExpected` で初期状態を決め、`WKStylusDeviceObserverChangeTimeInterval` のユーザーデフォルトがあれば `changeTimeInterval` を上書きする。

## References
- [`WKStylusDeviceObserver.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKStylusDeviceObserver.h#L32)
- [`WKStylusDeviceObserver.mm#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKStylusDeviceObserver.mm#L51)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
