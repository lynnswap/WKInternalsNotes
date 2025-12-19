# ``WKInternalsNotes/WKContentView/clearTextIndicator(_:)``

テキストインジケータを消去する。

## Objective-C Declaration
```objective-c
- (void)clearTextIndicator:(WebCore::TextIndicatorDismissalAnimation)animation;
```

## Discussion
フェードアウト中は何もしない。手動アニメーションが必要でフェードアウト指定の場合は `startFadeOut` を実行し、それ以外はレイヤーを破棄する。

## References
- [`WKContentViewInteraction.h#L931`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L931)
- [`WKContentViewInteraction.mm#L12595`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12595)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
