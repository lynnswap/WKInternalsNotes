# ``WKInternalsNotes/WKKeyboardScrollViewAnimatorDelegate/keyboardScrollViewAnimatorDidFinishScrolling(_:)``

キーボードスクロールの終了を通知する。

## Objective-C Declaration
```objective-c
- (void)keyboardScrollViewAnimatorDidFinishScrolling:(WKKeyboardScrollViewAnimator *)animator;
```

## Discussion
`WKContentView` では `_webView` に `- _didFinishScrolling:` を通知し、`_isKeyboardScrollingAnimationRunning` を `NO` に戻す。

## References
- [`WKKeyboardScrollingAnimator.h#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.h#L65)
- [`WKContentViewInteraction.mm#L7882`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7882)
- [`WKContentViewInteraction.mm#L7884`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7884)
- [`WKContentViewInteraction.mm#L7885`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7885)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
