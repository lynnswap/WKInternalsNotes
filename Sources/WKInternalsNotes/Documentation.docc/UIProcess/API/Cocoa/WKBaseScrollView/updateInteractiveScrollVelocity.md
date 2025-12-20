# ``WKInternalsNotes/WKBaseScrollView/updateInteractiveScrollVelocity()``

インタラクティブスクロール速度の更新を行う。

## Objective-C Declaration
```objective-c
- (void)updateInteractiveScrollVelocity;
```

## Discussion
`tracking` または `decelerating` でない場合は何もしない。スクロール中は `contentOffset` を `_scrollingDeltaWindow` に記録する。

## References
- [`WKBaseScrollView.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.h#L59)
- [`WKBaseScrollView.mm#L244`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.mm#L244)
- [`WKBaseScrollView.mm#L249`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.mm#L249)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
