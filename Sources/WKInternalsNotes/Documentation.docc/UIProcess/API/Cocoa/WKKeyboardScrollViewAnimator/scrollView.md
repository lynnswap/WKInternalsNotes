# ``WKInternalsNotes/WKKeyboardScrollViewAnimator/scrollView()``

現在のスクロール対象を返す。

## Objective-C Declaration
```objective-c
- (WKBaseScrollView *)scrollView;
```

## Discussion
`beginWithEvent:scrollView:` で保持した `WKBaseScrollView` を返す。

## References
- [`WKKeyboardScrollingAnimator.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.h#L56)
- [`WKKeyboardScrollingAnimator.mm#L636`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L636)
- [`WKKeyboardScrollingAnimator.mm#L638`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L638)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
