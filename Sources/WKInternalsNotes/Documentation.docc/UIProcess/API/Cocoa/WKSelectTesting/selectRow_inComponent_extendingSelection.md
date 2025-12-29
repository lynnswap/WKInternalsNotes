# ``WKInternalsNotes/WKSelectTesting/selectRow(_:inComponent:extendingSelection:)``

テスト用に指定行を選択する。

## Objective-C Declaration
```objective-c
- (void)selectRow:(NSInteger)rowIndex inComponent:(NSInteger)componentIndex extendingSelection:(BOOL)extendingSelection;
```

## Discussion
現在の実装では `extendingSelection` は未対応（FIXME）で、選択後に必要な delegate 呼び出しや UI 更新を行う。

## References
- [`WKFormSelectPicker.mm#L332`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.mm#L332)
- [`WKFormSelectPicker.mm#L484`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.mm#L484)
- [`WKFormSelectPicker.mm#L736`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.mm#L736)
- [`WKFormSelectControl.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.h#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
