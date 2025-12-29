# ``WKInternalsNotes/WKKeyboardScrollableInternal/rubberbandableDirections()``

ラバーバンド可能な方向を返す。

## Objective-C Declaration
```objective-c
- (WebCore::RectEdges<bool>)rubberbandableDirections;
```

## Discussion
`_wk_canScrollVerticallyWithoutBouncing` と `_wk_canScrollHorizontallyWithoutBouncing` を使って上下左右の可否を設定する。

## References
- [`WKKeyboardScrollingAnimator.mm#L742`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.mm#L742)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
