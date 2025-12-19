# ``WKInternalsNotes/WKContentView/selectFormAccessoryHasCheckedItemAtRow(_:)``

フォーム選択アクセサリで指定行がチェック済みかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)selectFormAccessoryHasCheckedItemAtRow:(long)rowIndex;
```

## Discussion
`PEPPER_UI_CORE` が無効で、`_inputPeripheral` が `WKFormSelectControl` の場合に `selectFormAccessoryHasCheckedItemAtRow:` を呼ぶ。該当しない場合は `NO`。

## References
- [`WKContentViewInteraction.h#L1034`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1034)
- [`WKContentViewInteraction.mm#L14504`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14504)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
