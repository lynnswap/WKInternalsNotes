# ``WKInternalsNotes/WKFullScreenViewController/setAnimatingViewAlpha(_:)``

アニメーション用ビューの透明度を変更する。

## Objective-C Declaration
```objective-c
- (void)setAnimatingViewAlpha:(CGFloat)alpha;
```

## Discussion
`pipHideAnimationDuration` でアニメーションしながら `_animatingView` の `alpha` を更新する。

## References
- [`WKFullScreenViewController.mm#L574`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L574)
- [`WKFullScreenViewController.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L64)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
