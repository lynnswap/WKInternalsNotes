# ``WKInternalsNotes/WKFocusedFormControlViewDelegate/hasPreviousNodeForFocusedFormControlView(_:)``

前のノードが存在するかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)hasPreviousNodeForFocusedFormControlView:(WKFocusedFormControlView *)view;
```

## Discussion
`reloadData:` が `hasPreviousNodeForFocusedFormControlView:` を呼び出し、`hasPreviousNode` に反映する。

## References
- [`WKFocusedFormControlView.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L44)
- [`WKFocusedFormControlView.mm#L272`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L272)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
