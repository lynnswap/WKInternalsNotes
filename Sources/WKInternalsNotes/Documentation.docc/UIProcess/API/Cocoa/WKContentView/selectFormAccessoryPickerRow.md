# ``WKInternalsNotes/WKContentView/selectFormAccessoryPickerRow(_:)``

フォーム選択 UI の指定行を選択する。

## Objective-C Declaration
```objective-c
- (void)selectFormAccessoryPickerRow:(NSInteger)rowIndex;
```

## Discussion
`PEPPER_UI_CORE` が有効なら `WKSelectMenuListViewController` に行選択を委譲し、無効なら `WKFormSelectControl` に対して `selectRow:inComponent:extendingSelection:` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L1033`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1033)
- [`WKContentViewInteraction.mm#L14493`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14493)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
