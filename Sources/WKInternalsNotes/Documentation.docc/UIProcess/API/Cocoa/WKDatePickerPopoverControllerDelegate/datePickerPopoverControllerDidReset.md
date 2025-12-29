# ``WKInternalsNotes/WKDatePickerPopoverControllerDelegate/datePickerPopoverControllerDidReset(_:)``

日付ピッカーのリセット操作を通知する。

## Objective-C Declaration
```objective-c
- (void)datePickerPopoverControllerDidReset:(WKDatePickerPopoverController *)controller;
```

## Discussion
`resetDatePicker` の実行時に delegate が呼ばれる。

## References
- [`WKDatePickerPopoverController.mm#L271`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerPopoverController.mm#L271)
- [`WKDatePickerPopoverController.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerPopoverController.h#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
