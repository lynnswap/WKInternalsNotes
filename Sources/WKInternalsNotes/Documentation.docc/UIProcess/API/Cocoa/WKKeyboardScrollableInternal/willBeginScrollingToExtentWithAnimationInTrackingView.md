# ``WKInternalsNotes/WKKeyboardScrollableInternal/willBeginScrollingToExtentWithAnimationInTrackingView(_:)``

スクロール範囲へのアニメーション開始前にトラッキング用ビューを追加する。

## Objective-C Declaration
```objective-c
- (void)willBeginScrollingToExtentWithAnimationInTrackingView:(UIView *)view;
```

## Discussion
`scrollView` に `view` を追加し、スクロールインジケータを点滅表示する。

## References
- [`WKKeyboardScrollingAnimator.mm#L695`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L695)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
