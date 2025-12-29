# ``WKInternalsNotes/WKDatePickerPopoverController/dismissDatePicker()``

日付選択 UI をアニメーション付きで閉じる。

## Objective-C Declaration
```objective-c
- (void)dismissDatePicker;
```

## Discussion
内部で `dismissDatePickerAnimated:YES` を呼び出す。表示元の `presentingViewController` を `dismiss` し、完了時に `_dispatchPopoverControllerDidDismissIfNeeded` を行う。

## References
- [`WKDatePickerPopoverController.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerPopoverController.h#L45)
- [`WKDatePickerPopoverController.mm#L316`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerPopoverController.mm#L316)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
