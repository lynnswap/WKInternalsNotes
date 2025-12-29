# ``WKInternalsNotes/WKKeyboardScrollableInternal/scrollableDirectionsFromOffset(_:)``

指定オフセットからスクロール可能な方向を返す。

## Objective-C Declaration
```objective-c
- (WebCore::RectEdges<bool>)scrollableDirectionsFromOffset:(CGPoint)offset;
```

## Discussion
`adjustedContentInset` と `contentSize`、`bounds` から最小/最大の contentOffset を算出し、上下左右それぞれがスクロール可能かを `RectEdges<bool>` で返す。

## References
- [`WKKeyboardScrollingAnimator.mm#L719`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L719)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
