# ``WKInternalsNotes/WKContentView/dateTimeInputControl``

日付/時刻入力コントロールを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKDateTimeInputControl *dateTimeInputControl;
```

## Default Value
`_inputPeripheral` が `WKDateTimeInputControl` の場合に返す。

## Discussion
watchOS 以外で `_inputPeripheral` が `WKDateTimeInputControl` のときにキャストして返し、それ以外は `nil`。

## References
- [`WKContentViewInteraction.h#L1065`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1065)
- [`WKContentViewInteraction.mm#L14428`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14428)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
