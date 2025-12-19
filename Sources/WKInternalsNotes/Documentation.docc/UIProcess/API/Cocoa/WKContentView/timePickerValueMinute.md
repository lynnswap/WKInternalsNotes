# ``WKInternalsNotes/WKContentView/timePickerValueMinute()``

時刻ピッカーの分（minute）を返す。

## Objective-C Declaration
```objective-c
- (double)timePickerValueMinute;
```

## Discussion
watchOS 以外で `_inputPeripheral` が `WKDateTimeInputControl` の場合に `timePickerValueMinute` を返し、それ以外は `-1`。

## References
- [`WKContentViewInteraction.h#L1038`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1038)
- [`WKContentViewInteraction.mm#L14573`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14573)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
