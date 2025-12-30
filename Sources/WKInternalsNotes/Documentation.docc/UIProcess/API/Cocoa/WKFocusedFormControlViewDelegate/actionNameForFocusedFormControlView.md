# ``WKInternalsNotes/WKFocusedFormControlViewDelegate/actionNameForFocusedFormControlView(_:)``

送信ボタンの表示名を返す。

## Objective-C Declaration
```objective-c
- (NSString *)actionNameForFocusedFormControlView:(WKFocusedFormControlView *)view;
```

## Discussion
`reloadData:` が `actionNameForFocusedFormControlView:` を呼び出して `submitActionName` を更新する。

## References
- [`WKFocusedFormControlView.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L38)
- [`WKFocusedFormControlView.mm#L272`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L272)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
