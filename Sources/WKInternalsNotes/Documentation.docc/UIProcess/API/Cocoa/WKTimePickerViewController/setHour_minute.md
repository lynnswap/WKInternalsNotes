# ``WKInternalsNotes/WKTimePickerViewController/setHour(_:minute:)``

時刻を設定して確定処理を呼ぶ。

## Objective-C Declaration
```objective-c
- (void)setHour:(NSInteger)hour minute:(NSInteger)minute;
```

## Discussion
`_timePicker` に時刻を反映し、そのまま `rightButtonWOTAction` を呼んで確定処理を実行する。

## References
- [`WKTimePickerViewController.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTimePickerViewController.h#L41)
- [`WKTimePickerViewController.mm#L129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTimePickerViewController.mm#L129)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
