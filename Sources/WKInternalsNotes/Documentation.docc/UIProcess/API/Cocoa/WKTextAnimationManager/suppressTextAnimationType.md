# ``WKInternalsNotes/WKTextAnimationManager/suppressTextAnimationType()``

既存のテキストアニメーションを一時的に抑制する。

## Objective-C Declaration
```objective-c
- (void)suppressTextAnimationType;
```

## Discussion
`_chunkToEffect` の各エフェクトを `removeEffect:` で取り除き、`Initial` 以外のタイプは辞書から削除する。

## References
- [`WKTextAnimationManagerMac.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextAnimationManagerMac.h#L50)
- [`WKTextAnimationManagerMac.mm#L207`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextAnimationManagerMac.mm#L207)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
