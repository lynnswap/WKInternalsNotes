# ``WKInternalsNotes/WKContentView/_simulateModelInteractionPanGestureBeginAtPoint(_:)``

モデル操作のパン開始をシミュレートする。

## Objective-C Declaration
```objective-c
- (void)_simulateModelInteractionPanGestureBeginAtPoint:(CGPoint)hitPoint;
```

## Discussion
`ENABLE(MODEL_PROCESS)` のとき `modelInteractionPanGestureDidBeginAtPoint:` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L1045`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1045)
- [`WKContentViewInteraction.mm#L14643`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14643)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
