# ``WKInternalsNotes/WKDeferringGestureRecognizer/shouldDeferGestureRecognizer(_:)``

指定のジェスチャを遅延すべきか判定する。

## Objective-C Declaration
```objective-c
- (BOOL)shouldDeferGestureRecognizer:(UIGestureRecognizer *)gestureRecognizer;
```

## Discussion
`deferringGestureRecognizer:shouldDeferOtherGestureRecognizer:` をデリゲートに委譲する。

## References
- [`WKDeferringGestureRecognizer.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKDeferringGestureRecognizer.h#L50)
- [`WKDeferringGestureRecognizer.mm#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKDeferringGestureRecognizer.mm#L82)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
