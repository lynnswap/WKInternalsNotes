# ``WKInternalsNotes/WKContentView/removeTextAnimationForAnimationID(_:)``

テキストアニメーションを解除する。

## Objective-C Declaration
```objective-c
- (void)removeTextAnimationForAnimationID:(NSUUID *)uuid;
```

## Discussion
ID が無い場合や設定無効時、マネージャ未生成時は何もしない。条件が揃えば登録済みのアニメーションを削除する。

## References
- [`WKContentViewInteraction.h#L936`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L936)
- [`WKContentViewInteraction.mm#L14175`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14175)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
