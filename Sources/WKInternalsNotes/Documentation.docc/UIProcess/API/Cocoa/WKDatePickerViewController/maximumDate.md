# ``WKInternalsNotes/WKDatePickerViewController/maximumDate``

選択可能な最大日付を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSDate *maximumDate;
```

## Default Value
`viewDidLoad` で `defaultMaximumDate` が設定される。

## Discussion
setter は同値の場合に何もしない。値が変わると `_maximumDate` をコピーして保持する。

## References
- [`WKDatePickerViewController.mm#L118`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.mm#L118)
- [`WKDatePickerViewController.mm#L266`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.mm#L266)
- [`WKDatePickerViewController.mm#L467`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.mm#L467)
- [`WKDatePickerViewController.mm#L478`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.mm#L478)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
