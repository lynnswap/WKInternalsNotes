# ``WKInternalsNotes/WKMouseInteraction/_updateMouseTouches(_:)``

マウスタッチの状態を更新し、必要ならイベントを通知する。

## Objective-C Declaration
```objective-c
- (void)_updateMouseTouches:(NSSet<UITouch *> *)touches;
```

## Discussion
`touches` から現在のタッチを取得し、`phase` に応じて `MouseDown/MouseMove/MouseUp` を決定する。`createMouseEventWithType` でイベントを生成し、生成できた場合のみ delegate に通知する。`MouseUp` の場合は `_touching` と `_pressedButtonMask` をリセットする。

## References
- [`WKMouseInteraction.mm#L388`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L388)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
