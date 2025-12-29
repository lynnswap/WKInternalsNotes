# ``WKInternalsNotes/WKDateTimeInputControl/initWithView(_:)``

対象要素の種類に応じた日時入力コントロールを生成する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithView:(WKContentView *)view;
```

## Discussion
`focusedElementInformation.elementType` を見て `WKDateTimePicker` を生成し、対応外の型では `nil` を返す。

## References
- [`WKDateTimeInputControl.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDateTimeInputControl.h#L33)
- [`WKDateTimeInputControl.mm#L400`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDateTimeInputControl.mm#L400)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
