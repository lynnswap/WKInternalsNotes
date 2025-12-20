# ``WKInternalsNotes/WKBaseScrollView/interactiveScrollVelocityInPointsPerSecond``

インタラクティブスクロール中の速度を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGSize interactiveScrollVelocityInPointsPerSecond;
```

## Default Value
更新が無い場合は `CGSizeZero`。

## Discussion
`_scrollingDeltaWindow` の平均速度を返す。更新が古い場合や更新が無い場合は `CGSizeZero` になる。

## References
- [`WKBaseScrollView.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.h#L57)
- [`WKBaseScrollView.mm#L244`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.mm#L244)
- [`WKBaseScrollView.mm#L254`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.mm#L254)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
