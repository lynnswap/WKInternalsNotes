# ``WKInternalsNotes/WKFormSelectControl/selectRow(_:inComponent:extendingSelection:)``

テスト用に選択行の変更を委譲する。

## Objective-C Declaration
```objective-c
- (void)selectRow:(NSInteger)rowIndex inComponent:(NSInteger)componentIndex extendingSelection:(BOOL)extendingSelection;
```

## Discussion
`control` が `selectRow:inComponent:extendingSelection:` に応答できる場合のみ、`WKSelectTesting` としてそのまま転送する。

## References
- [`WKFormSelectControl.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.h#L43)
- [`WKFormSelectControl.mm#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.mm#L103)
- [`WKFormSelectControl.mm#L105`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.mm#L105)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
