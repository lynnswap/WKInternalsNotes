# ``WKInternalsNotes/WKKeyboardScrollViewAnimator/stopScrollingImmediately()``

スクロールを即座に停止する。

## Objective-C Declaration
```objective-c
- (void)stopScrollingImmediately;
```

## Discussion
内部の `WKKeyboardScrollingAnimator` に停止処理を委譲する。

## References
- [`WKKeyboardScrollingAnimator.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.h#L52)
- [`WKKeyboardScrollingAnimator.mm#L592`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L592)
- [`WKKeyboardScrollingAnimator.mm#L594`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L594)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
