# ``WKInternalsNotes/WKKeyboardScrollViewAnimator/scrollTriggeringKeyIsPressed()``

スクロール開始キーが押されているかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)scrollTriggeringKeyIsPressed;
```

## Discussion
内部の `WKKeyboardScrollingAnimator` の状態をそのまま返す。

## References
- [`WKKeyboardScrollingAnimator.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.h#L50)
- [`WKKeyboardScrollingAnimator.mm#L646`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L646)
- [`WKKeyboardScrollingAnimator.mm#L648`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L648)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
