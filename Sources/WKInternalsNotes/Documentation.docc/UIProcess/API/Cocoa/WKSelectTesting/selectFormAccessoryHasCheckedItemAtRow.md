# ``WKInternalsNotes/WKSelectTesting/selectFormAccessoryHasCheckedItemAtRow(_:)``

指定行がチェック状態かを返す。

## Objective-C Declaration
```objective-c
- (BOOL)selectFormAccessoryHasCheckedItemAtRow:(long)rowIndex;
```

## Discussion
行番号が範囲外の場合は `NO`。コンテキストメニュー利用時は `UIAction` の state を参照する。

## References
- [`WKFormSelectPicker.mm#L342`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.mm#L342)
- [`WKFormSelectPicker.mm#L747`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.mm#L747)
- [`WKFormSelectControl.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.h#L44)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
