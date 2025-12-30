# ``WKInternalsNotes/WKFocusedFormControlViewDelegate/focusedFormControlViewDidRequestNextNode(_:)``

次のノードへの移動要求時に呼ばれる。

## Objective-C Declaration
```objective-c
- (void)focusedFormControlViewDidRequestNextNode:(WKFocusedFormControlView *)view;
```

## Discussion
クラウン入力のオフセットが閾値を超え、`hasNextNode` が真のときに呼ばれる。

## References
- [`WKFocusedFormControlView.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L41)
- [`WKFocusedFormControlView.mm#L360`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L360)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
