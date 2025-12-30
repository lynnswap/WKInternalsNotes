# ``WKInternalsNotes/WKTextAnimationManager/addTextAnimationForAnimationID(_:withData:)``

指定 ID のテキストアニメーションを登録する。

## Objective-C Declaration
```objective-c
- (void)addTextAnimationForAnimationID:(NSUUID *)uuid withData:(const WebCore::TextAnimationData&)data;
```

## Discussion
`Initial` かつ置換完了済みの場合は処理を打ち切る。それ以外は `style` に応じた `_WTTextEffect` を生成して `_effectView` に追加し、`_chunkToEffect` に `effectID` とタイプを保持する。完了時は `removeTextAnimationForAnimationID:` と `hideTextAnimationView` を呼び出す。

## References
- [`WKTextAnimationManagerMac.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextAnimationManagerMac.h#L43)
- [`WKTextAnimationManagerMac.mm#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextAnimationManagerMac.mm#L91)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
