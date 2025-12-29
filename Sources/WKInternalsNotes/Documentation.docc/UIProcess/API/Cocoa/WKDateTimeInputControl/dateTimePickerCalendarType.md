# ``WKInternalsNotes/WKDateTimeInputControl/dateTimePickerCalendarType``

日付ピッカーのカレンダー種別を返す（テスト用）。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *dateTimePickerCalendarType;
```

## Default Value
`WKDateTimePicker` の `calendarType`。取得できない場合は `nil`。

## Discussion
`WKDateTimePicker` を取得できた場合に `calendarType` を返す。

## References
- [`WKDateTimeInputControl.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDateTimeInputControl.h#L37)
- [`WKDateTimeInputControl.mm#L430`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDateTimeInputControl.mm#L430)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
