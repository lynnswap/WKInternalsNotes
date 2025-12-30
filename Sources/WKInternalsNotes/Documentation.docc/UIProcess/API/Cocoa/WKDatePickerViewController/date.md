# ``WKInternalsNotes/WKDatePickerViewController/date``

現在選択中の日付を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSDate *date;
```

## Default Value
`viewDidLoad` で初期値が設定される。

## Discussion
setter は `minimumDate`/`maximumDate` の範囲にクランプし、日付成分を更新する。getter はキャッシュがなければ `day/month/year/era` から生成する。

## References
- [`WKDatePickerViewController.mm#L116`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.mm#L116)
- [`WKDatePickerViewController.mm#L267`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.mm#L267)
- [`WKDatePickerViewController.mm#L483`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.mm#L483)
- [`WKDatePickerViewController.mm#L511`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.mm#L511)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
