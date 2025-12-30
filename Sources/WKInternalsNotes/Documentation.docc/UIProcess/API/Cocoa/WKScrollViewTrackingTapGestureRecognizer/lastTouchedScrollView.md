# ``WKInternalsNotes/WKScrollViewTrackingTapGestureRecognizer/lastTouchedScrollView``

最後にタッチされた `UIScrollView` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, weak) UIScrollView *lastTouchedScrollView;
```

## Default Value
初期値は `nil`。

## Discussion
`touchesBegan` で `scrollViewForTouches` から取得して設定し、`reset` で `nil` に戻す。

## References
- [`WKScrollViewTrackingTapGestureRecognizer.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollViewTrackingTapGestureRecognizer.h#L34)
- [`WKScrollViewTrackingTapGestureRecognizer.mm#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollViewTrackingTapGestureRecognizer.mm#L35)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
