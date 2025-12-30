# ``WKInternalsNotes/WKFocusedFormControlViewDelegate/scrollViewForFocusedFormControlView(_:)``

クラウン入力で操作する `UIScrollView` を返す。

## Objective-C Declaration
```objective-c
- (UIScrollView *)scrollViewForFocusedFormControlView:(WKFocusedFormControlView *)view;
```

## Discussion
`scrollViewForCrownInputSequencer` が delegate から取得して利用する。

## References
- [`WKFocusedFormControlView.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L47)
- [`WKFocusedFormControlView.mm#L348`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L348)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
