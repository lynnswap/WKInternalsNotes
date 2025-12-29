# ``WKInternalsNotes/WKDateTimeInputControl/timePickerValueHour``

時の値を返す（テスト用）。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) double timePickerValueHour;
```

## Default Value
`WKDateTimePicker` の `hour`。取得できない場合は `-1`。

## Discussion
`WKDateTimePicker` を取得できた場合に `hour` を返し、失敗時は `-1` を返す。

## References
- [`WKDateTimeInputControl.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDateTimeInputControl.h#L38)
- [`WKDateTimeInputControl.mm#L437`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDateTimeInputControl.mm#L437)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
