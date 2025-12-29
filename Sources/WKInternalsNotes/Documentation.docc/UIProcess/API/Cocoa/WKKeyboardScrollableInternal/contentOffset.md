# ``WKInternalsNotes/WKKeyboardScrollableInternal/contentOffset()``

現在の contentOffset を返す。

## Objective-C Declaration
```objective-c
- (CGPoint)contentOffset;
```

## Discussion
`scrollView` が無い場合は `CGPointZero`。それ以外は `scrollView.contentOffset` を返す。

## References
- [`WKKeyboardScrollingAnimator.mm#L701`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L701)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
