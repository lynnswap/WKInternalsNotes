# ``WKInternalsNotes/WKStylusDeviceObserver/stop()``

スタイラス状態の監視を停止する。

## Objective-C Declaration
```objective-c
- (void)stop;
```

## Discussion
開始カウントを減らし、最後の呼び出しでのみ `UIScribbleInteraction.isPencilInputExpected` の KVO 監視を解除する。

## References
- [`WKStylusDeviceObserver.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKStylusDeviceObserver.h#L35)
- [`WKStylusDeviceObserver.mm#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKStylusDeviceObserver.mm#L95)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
