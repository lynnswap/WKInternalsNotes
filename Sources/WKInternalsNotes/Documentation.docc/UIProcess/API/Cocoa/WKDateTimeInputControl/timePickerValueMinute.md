# ``WKInternalsNotes/WKDateTimeInputControl/timePickerValueMinute``

分の値を返す（テスト用）。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) double timePickerValueMinute;
```

## Default Value
`WKDateTimePicker` の `minute`。取得できない場合は `-1`。

## Discussion
`WKDateTimePicker` を取得できた場合に `minute` を返し、失敗時は `-1` を返す。

## References
- [`WKDateTimeInputControl.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDateTimeInputControl.h#L39)
- [`WKDateTimeInputControl.mm#L444`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDateTimeInputControl.mm#L444)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
