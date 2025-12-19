# ``WKInternalsNotes/WKContentView/modelInteractionPanGestureDidUpdateWithPoint(_:)``

モデル操作のパン更新を処理する。

## Objective-C Declaration
```objective-c
- (void)modelInteractionPanGestureDidUpdateWithPoint:(CGPoint)inputPoint;
```

## Discussion
ステージモードセッションがあり、準備中でなければ入力点の平行移動を `TransformationMatrix` に反映し、`stageModeSessionDidUpdate` で更新を通知する。

## References
- [`WKContentViewInteraction.h#L905`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L905)
- [`WKContentViewInteraction.mm#L11557`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11557)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
