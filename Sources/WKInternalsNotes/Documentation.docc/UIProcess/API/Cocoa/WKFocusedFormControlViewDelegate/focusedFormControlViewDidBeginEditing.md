# ``WKInternalsNotes/WKFocusedFormControlViewDelegate/focusedFormControlViewDidBeginEditing(_:)``

ハイライト領域のタップ時に呼ばれる。

## Objective-C Declaration
```objective-c
- (void)focusedFormControlViewDidBeginEditing:(WKFocusedFormControlView *)view;
```

## Discussion
`handleTap` がタップ位置を判定し、範囲内なら `focusedFormControlViewDidBeginEditing:` を呼び出す。

## References
- [`WKFocusedFormControlView.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L36)
- [`WKFocusedFormControlView.mm#L192`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L192)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
