# ``WKInternalsNotes/WKFormSelectControl/selectFormAccessoryHasCheckedItemAtRow(_:)``

指定行のチェック状態を問い合わせる。

## Objective-C Declaration
```objective-c
- (BOOL)selectFormAccessoryHasCheckedItemAtRow:(long)rowIndex;
```

## Discussion
`control` が `selectFormAccessoryHasCheckedItemAtRow:` に応答できる場合のみ、`WKSelectTesting` として呼び出して結果を返す。

## References
- [`WKFormSelectControl.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.h#L44)
- [`WKFormSelectControl.mm#L116`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.mm#L116)
- [`WKFormSelectControl.mm#L118`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.mm#L118)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
