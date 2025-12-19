# ``WKInternalsNotes/WKContentView/_simulateModelInteractionPanGestureUpdateAtPoint(_:)``

モデル操作のパン更新をシミュレートする。

## Objective-C Declaration
```objective-c
- (void)_simulateModelInteractionPanGestureUpdateAtPoint:(CGPoint)hitPoint;
```

## Discussion
`ENABLE(MODEL_PROCESS)` のとき `modelInteractionPanGestureDidUpdateWithPoint:` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L1046`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1046)
- [`WKContentViewInteraction.mm#L14648`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14648)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
