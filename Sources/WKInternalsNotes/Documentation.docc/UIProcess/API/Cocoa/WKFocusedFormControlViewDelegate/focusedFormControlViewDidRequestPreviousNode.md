# ``WKInternalsNotes/WKFocusedFormControlViewDelegate/focusedFormControlViewDidRequestPreviousNode(_:)``

前のノードへの移動要求時に呼ばれる。

## Objective-C Declaration
```objective-c
- (void)focusedFormControlViewDidRequestPreviousNode:(WKFocusedFormControlView *)view;
```

## Discussion
クラウン入力のオフセットが閾値を下回り、`hasPreviousNode` が真のときに呼ばれる。

## References
- [`WKFocusedFormControlView.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L42)
- [`WKFocusedFormControlView.mm#L360`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L360)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
