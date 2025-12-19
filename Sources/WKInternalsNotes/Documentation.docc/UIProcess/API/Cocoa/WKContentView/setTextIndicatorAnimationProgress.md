# ``WKInternalsNotes/WKContentView/setTextIndicatorAnimationProgress(_:)``

テキストインジケータのアニメーション進捗を設定する。

## Objective-C Declaration
```objective-c
- (void)setTextIndicatorAnimationProgress:(float)NSAnimationProgress;
```

## Discussion
`_textIndicator` が存在する場合に `WebTextIndicatorLayer` へ進捗を反映する。

## References
- [`WKContentViewInteraction.h#L930`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L930)
- [`WKContentViewInteraction.mm#L12610`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12610)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
