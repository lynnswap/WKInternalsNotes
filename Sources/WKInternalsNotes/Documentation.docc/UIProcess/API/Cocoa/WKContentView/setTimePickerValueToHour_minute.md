# ``WKInternalsNotes/WKContentView/setTimePickerValueToHour(_:minute:)``

時刻ピッカーに時刻値を設定する。

## Objective-C Declaration
```objective-c
- (void)setTimePickerValueToHour:(NSInteger)hour minute:(NSInteger)minute;
```

## Discussion
`PEPPER_UI_CORE` が有効なら `WKTimePickerViewController` に `setHour:minute:` を呼び、無効なら `WKDateTimeInputControl` に `setTimePickerHour:minute:` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L1036`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1036)
- [`WKContentViewInteraction.mm#L14553`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14553)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
