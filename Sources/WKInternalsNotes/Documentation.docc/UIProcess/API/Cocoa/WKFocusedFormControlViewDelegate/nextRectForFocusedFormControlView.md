# ``WKInternalsNotes/WKFocusedFormControlViewDelegate/nextRectForFocusedFormControlView(_:)``

次のノードの矩形を返す。

## Objective-C Declaration
```objective-c
- (CGRect)nextRectForFocusedFormControlView:(WKFocusedFormControlView *)view;
```

## Discussion
`reloadData:` が `nextRectForFocusedFormControlView:` を呼び出し、`nextHighlightedFrame` に反映する。

## References
- [`WKFocusedFormControlView.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L45)
- [`WKFocusedFormControlView.mm#L272`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L272)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
