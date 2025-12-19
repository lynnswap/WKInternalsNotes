# ``WKInternalsNotes/WKContentView/timePickerValueHour()``

時刻ピッカーの時（hour）を返す。

## Objective-C Declaration
```objective-c
- (double)timePickerValueHour;
```

## Discussion
watchOS 以外で `_inputPeripheral` が `WKDateTimeInputControl` の場合に `timePickerValueHour` を返し、それ以外は `-1`。

## References
- [`WKContentViewInteraction.h#L1037`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1037)
- [`WKContentViewInteraction.mm#L14564`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14564)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
