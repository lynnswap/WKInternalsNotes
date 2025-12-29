# ``WKInternalsNotes/WKFullScreenWindowController/_startEnterFullScreenAnimationWithDuration(_:)``

フルスクリーン突入時のズーム/マスク/フェードのアニメーションを開始する。

## Objective-C Declaration
```objective-c
- (void)_startEnterFullScreenAnimationWithDuration:(NSTimeInterval)duration;
```

## Discussion
`_initialFrame`/`_finalFrame` と画面サイズからアニメーションを作成し、`_clipView` の `layer` にズーム、`mask` にマスクアニメーション、背景レイヤにフェードを追加する。`CATransaction` でアクションを無効化し、レイヤー状態の更新のみを行う。

## References
- [`WKFullScreenWindowController.mm#L1041`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L1041)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
