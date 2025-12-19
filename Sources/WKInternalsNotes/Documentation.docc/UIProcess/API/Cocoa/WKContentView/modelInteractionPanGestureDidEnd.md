# ``WKInternalsNotes/WKContentView/modelInteractionPanGestureDidEnd()``

モデル操作のパン終了を処理する。

## Objective-C Declaration
```objective-c
- (void)modelInteractionPanGestureDidEnd;
```

## Discussion
準備中でないステージモードセッションがあれば `stageModeSessionDidEnd` で終了を通知し、`cleanUpStageModeSessionState` でセッション状態を破棄する。

## References
- [`WKContentViewInteraction.h#L906`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L906)
- [`WKContentViewInteraction.mm#L11567`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11567)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
