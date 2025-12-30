# ``WKInternalsNotes/WKFocusedFormControlViewDelegate/previousRectForFocusedFormControlView(_:)``

前のノードの矩形を返す。

## Objective-C Declaration
```objective-c
- (CGRect)previousRectForFocusedFormControlView:(WKFocusedFormControlView *)view;
```

## Discussion
`reloadData:` が `previousRectForFocusedFormControlView:` を呼び出し、`previousHighlightedFrame` に反映する。

## References
- [`WKFocusedFormControlView.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L46)
- [`WKFocusedFormControlView.mm#L272`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L272)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
