# ``WKInternalsNotes/WKKeyboardScrollViewAnimator/willStartInteractiveScroll()``

インタラクティブスクロール開始を通知する。

## Objective-C Declaration
```objective-c
- (void)willStartInteractiveScroll;
```

## Discussion
内部の `WKKeyboardScrollingAnimator` にそのまま委譲する。

## References
- [`WKKeyboardScrollingAnimator.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.h#L45)
- [`WKKeyboardScrollingAnimator.mm#L607`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L607)
- [`WKKeyboardScrollingAnimator.mm#L609`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L609)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
