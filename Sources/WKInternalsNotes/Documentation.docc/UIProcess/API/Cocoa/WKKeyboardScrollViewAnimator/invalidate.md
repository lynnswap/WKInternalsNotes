# ``WKInternalsNotes/WKKeyboardScrollViewAnimator/invalidate()``

内部状態を無効化する。

## Objective-C Declaration
```objective-c
- (void)invalidate;
```

## Discussion
保持している `scrollView` を `nil` にし、内部の `WKKeyboardScrollingAnimator` を `invalidate` したうえで解放する。

## References
- [`WKKeyboardScrollingAnimator.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.h#L43)
- [`WKKeyboardScrollingAnimator.mm#L584`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L584)
- [`WKKeyboardScrollingAnimator.mm#L586`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L586)
- [`WKKeyboardScrollingAnimator.mm#L588`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L588)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
