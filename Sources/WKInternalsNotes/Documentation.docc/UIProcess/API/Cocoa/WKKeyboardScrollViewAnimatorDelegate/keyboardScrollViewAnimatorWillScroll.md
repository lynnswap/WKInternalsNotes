# ``WKInternalsNotes/WKKeyboardScrollViewAnimatorDelegate/keyboardScrollViewAnimatorWillScroll(_:)``

キーボードスクロールの開始を通知する。

## Objective-C Declaration
```objective-c
- (void)keyboardScrollViewAnimatorWillScroll:(WKKeyboardScrollViewAnimator *)animator;
```

## Discussion
`WKContentView` では、`_isKeyboardScrollingAnimationRunning` を `YES` にして `willStartZoomOrScroll` を呼び出す。

## References
- [`WKKeyboardScrollingAnimator.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.h#L64)
- [`WKContentViewInteraction.mm#L7876`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7876)
- [`WKContentViewInteraction.mm#L7878`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7878)
- [`WKContentViewInteraction.mm#L7879`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7879)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
