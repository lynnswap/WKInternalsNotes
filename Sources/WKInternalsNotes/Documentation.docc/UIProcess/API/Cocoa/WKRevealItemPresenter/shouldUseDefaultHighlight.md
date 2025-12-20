# ``WKInternalsNotes/WKRevealItemPresenter/shouldUseDefaultHighlight``

デフォルトのハイライトを使うかどうかを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL shouldUseDefaultHighlight;
```

## Default Value
明示的な初期化がなく、生成直後はゼロ初期化のままになる。

## Discussion
`revealContext:shouldUseDefaultHighlightForItem:` でこの値をそのまま返し、Reveal のハイライト方式を切り替える。

## References
- [`WKRevealItemPresenter.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKRevealItemPresenter.h#L44)
- [`WKRevealItemPresenter.mm#L108`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKRevealItemPresenter.mm#L108)
- [`WKRevealItemPresenter.mm#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKRevealItemPresenter.mm#L110)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
