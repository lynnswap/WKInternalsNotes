# ``WKInternalsNotes/WKKeyboardScrollableInternal/scrollToContentOffset(_:animated:)``

指定されたオフセットにスクロールする。

## Objective-C Declaration
```objective-c
- (void)scrollToContentOffset:(WebCore::FloatPoint)offset animated:(BOOL)animated;
```

## Discussion
`scrollView` が無い場合は何もしない。delegate が `keyboardScrollViewAnimatorWillScroll:` に応答できる場合は通知し、その後 `_wk_setContentOffsetAndShowScrollIndicators:animated:` を呼ぶ。

## References
- [`WKKeyboardScrollingAnimator.mm#L686`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L686)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
