# ``WKInternalsNotes/WKDatePickerPopoverControllerDelegate/datePickerPopoverControllerDidDismiss(_:)``

ポップオーバーが閉じられたことを通知する。

## Objective-C Declaration
```objective-c
- (void)datePickerPopoverControllerDidDismiss:(WKDatePickerPopoverController *)controller;
```

## Discussion
`dismissDatePicker` の完了時や `UIPopoverPresentationController` の dismissal 時に、一度だけ呼ばれる。

## References
- [`WKDatePickerPopoverController.mm#L490`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerPopoverController.mm#L490)
- [`WKDatePickerPopoverController.mm#L503`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerPopoverController.mm#L503)
- [`WKDatePickerPopoverController.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerPopoverController.h#L35)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
