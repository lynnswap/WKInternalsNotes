# ``WKInternalsNotes/WKDatePickerViewController/minimumDate``

選択可能な最小日付を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSDate *minimumDate;
```

## Default Value
`viewDidLoad` で `defaultMinimumDate` が設定される。

## Discussion
setter は同値の場合に何もしない。値が変わると `_minimumDate` をコピーして保持する。

## References
- [`WKDatePickerViewController.mm#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.mm#L117)
- [`WKDatePickerViewController.mm#L265`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.mm#L265)
- [`WKDatePickerViewController.mm#L451`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.mm#L451)
- [`WKDatePickerViewController.mm#L462`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.mm#L462)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
