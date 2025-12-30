# ``WKInternalsNotes/WKFocusedFormControlViewDelegate/focusedFormControlViewDidCancel(_:)``

キャンセル操作時に呼ばれる。

## Objective-C Declaration
```objective-c
- (void)focusedFormControlViewDidCancel:(WKFocusedFormControlView *)view;
```

## Discussion
`didDismiss` から delegate を呼び出す。

## References
- [`WKFocusedFormControlView.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L35)
- [`WKFocusedFormControlView.mm#L210`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L210)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
