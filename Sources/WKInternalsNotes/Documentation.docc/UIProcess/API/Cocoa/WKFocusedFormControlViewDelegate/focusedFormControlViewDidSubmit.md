# ``WKInternalsNotes/WKFocusedFormControlViewDelegate/focusedFormControlViewDidSubmit(_:)``

送信操作時に呼ばれる。

## Objective-C Declaration
```objective-c
- (void)focusedFormControlViewDidSubmit:(WKFocusedFormControlView *)view;
```

## Discussion
`didSubmit` から delegate を呼び出す。

## References
- [`WKFocusedFormControlView.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L34)
- [`WKFocusedFormControlView.mm#L215`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L215)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
