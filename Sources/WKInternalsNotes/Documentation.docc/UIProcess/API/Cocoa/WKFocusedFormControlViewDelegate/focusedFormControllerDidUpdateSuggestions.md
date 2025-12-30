# ``WKInternalsNotes/WKFocusedFormControlViewDelegate/focusedFormControllerDidUpdateSuggestions(_:)``

サジェスト更新時に呼ばれる。

## Objective-C Declaration
```objective-c
- (void)focusedFormControllerDidUpdateSuggestions:(WKFocusedFormControlView *)view;
```

## Discussion
`setSuggestions:` が新しい候補を保持した後に delegate を通知する。

## References
- [`WKFocusedFormControlView.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L49)
- [`WKFocusedFormControlView.mm#L462`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L462)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
