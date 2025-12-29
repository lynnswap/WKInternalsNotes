# ``WKInternalsNotes/WKDatePickerPopoverController/initWithDatePicker(_:delegate:)``

`UIDatePicker` を内包するコンテンツビューで初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithDatePicker:(UIDatePicker *)datePicker delegate:(id<WKDatePickerPopoverControllerDelegate>)delegate;
```

## Discussion
`[super init]` に成功した場合、`WKDatePickerContentView` を生成して `delegate` を保持する。ポップオーバー表示を使う構成では `modalPresentationStyle` と `popoverPresentationController.delegate` を設定する。

## References
- [`WKDatePickerPopoverController.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerPopoverController.h#L40)
- [`WKDatePickerPopoverController.mm#L239`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerPopoverController.mm#L239)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
