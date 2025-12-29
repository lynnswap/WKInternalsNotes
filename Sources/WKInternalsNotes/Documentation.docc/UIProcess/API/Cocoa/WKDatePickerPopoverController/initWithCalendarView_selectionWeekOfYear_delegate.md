# ``WKInternalsNotes/WKDatePickerPopoverController/initWithCalendarView(_:selectionWeekOfYear:delegate:)``

`UICalendarView` と週選択を内包するコンテンツビューで初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithCalendarView:(UICalendarView *)calendarView selectionWeekOfYear:(UICalendarSelectionWeekOfYear *)weekSelection delegate:(id<WKDatePickerPopoverControllerDelegate>)delegate;
```

## Discussion
`[super init]` に成功した場合、`WKDatePickerContentView` を `calendarView`/`weekSelection` で構築し `delegate` を保持する。ポップオーバー表示構成では `modalPresentationStyle` と `popoverPresentationController.delegate` を設定する。

## References
- [`WKDatePickerPopoverController.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerPopoverController.h#L42)
- [`WKDatePickerPopoverController.mm#L255`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerPopoverController.mm#L255)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
