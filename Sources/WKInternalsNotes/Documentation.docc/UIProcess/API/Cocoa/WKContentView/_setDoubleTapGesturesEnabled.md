# ``WKInternalsNotes/WKContentView/_setDoubleTapGesturesEnabled(_:)``

ダブルタップジェスチャの有効/無効を切り替える。

## Objective-C Declaration
```objective-c
- (void)_setDoubleTapGesturesEnabled:(BOOL)enabled;
```

## Discussion
再有効化時は新しいダブルタップ認識器を生成し、必要ならハイライト色を更新する。内部フラグを設定して `_updateDoubleTapGestureRecognizerEnablement` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L845`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L845)
- [`WKContentViewInteraction.mm#L6195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6195)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
