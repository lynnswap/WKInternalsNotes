# ``WKInternalsNotes/WKDateTimeInputControl/dismissWithAnimationForTesting()``

テスト用にピッカーをアニメーションで閉じる。

## Objective-C Declaration
```objective-c
- (BOOL)dismissWithAnimationForTesting;
```

## Discussion
`WKDateTimePicker` が存在する場合はアクセサリビューのヒットテストを確認し、`dismissDatePicker` を呼んで `YES` を返す。

## References
- [`WKDateTimeInputControl.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDateTimeInputControl.h#L41)
- [`WKDateTimeInputControl.mm#L451`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDateTimeInputControl.mm#L451)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
