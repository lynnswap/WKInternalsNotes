# ``WKInternalsNotes/WKKeyboardScrollableInternal/boundedContentOffset(_:)``

スクロール範囲内にクランプした offset を返す。

## Objective-C Declaration
```objective-c
- (CGPoint)boundedContentOffset:(CGPoint)offset;
```

## Discussion
`_wk_clampToScrollExtents:` の結果を返す。

## References
- [`WKKeyboardScrollingAnimator.mm#L709`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L709)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
