# ``WKInternalsNotes/WKKeyboardScrollViewAnimator/handleKeyEvent(_:)``

キーボードイベントを処理する。

## Objective-C Declaration
```objective-c
- (void)handleKeyEvent:(::WebEvent *)event;
```

## Discussion
内部の `WKKeyboardScrollingAnimator` にそのまま委譲する。

## References
- [`WKKeyboardScrollingAnimator.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.h#L48)
- [`WKKeyboardScrollingAnimator.mm#L641`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L641)
- [`WKKeyboardScrollingAnimator.mm#L643`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L643)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
