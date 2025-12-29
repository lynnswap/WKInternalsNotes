# ``WKInternalsNotes/WKMouseInteractionDelegate/mouseInteraction(_:changedWithEvent:)``

マウスイベントの変化を通知する。

## Objective-C Declaration
```objective-c
- (void)mouseInteraction:(WKMouseInteraction *)interaction changedWithEvent:(const WebKit::NativeWebMouseEvent&)event;
```

## Discussion
ホバー/マウスタッチの更新やポインタロック時の移動で `NativeWebMouseEvent` を生成し、このデリゲートメソッドが呼ばれる。

## References
- [`WKMouseInteraction.mm#L385`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L385)
- [`WKMouseInteraction.mm#L422`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L422)
- [`WKMouseInteraction.mm#L510`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L510)
- [`WKMouseInteraction.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.h#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
