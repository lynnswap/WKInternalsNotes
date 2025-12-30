# ``WKInternalsNotes/WKDatePickerViewController/didBeginInteractingWithDatePicker(_:)``

フォーカス中のピッカーを更新する。

## Objective-C Declaration
```objective-c
- (void)didBeginInteractingWithDatePicker:(WKDatePickerWheel *)datePicker;
```

## Discussion
同じ `datePicker` が既に `_focusedPicker` の場合は何もしない。各ピッカーのフォーカスアウトラインとラベル表示を切り替え、`_focusedPicker` を更新して `becomeFirstResponder` を呼ぶ。

## References
- [`WKDatePickerViewController.mm#L616`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.mm#L616)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
