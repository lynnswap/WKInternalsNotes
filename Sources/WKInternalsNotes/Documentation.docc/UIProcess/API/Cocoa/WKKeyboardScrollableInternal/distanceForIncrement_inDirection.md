# ``WKInternalsNotes/WKKeyboardScrollableInternal/distanceForIncrement(_:inDirection:)``

指定されたスクロール粒度・方向に対する移動距離を返す。

## Objective-C Declaration
```objective-c
- (CGFloat)distanceForIncrement:(WebCore::ScrollGranularity)increment inDirection:(WebCore::ScrollDirection)direction;
```

## Discussion
`scrollView` が無い場合は `0`。delegate 未実装なら `Document/Page/Line/Pixel` に応じて `contentSize` や `frame`、`zoomScale` を使ったデフォルト値を返す。delegate があれば `keyboardScrollViewAnimator:distanceForIncrement:inDirection:` の結果を返す。

## References
- [`WKKeyboardScrollingAnimator.mm#L658`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L658)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
