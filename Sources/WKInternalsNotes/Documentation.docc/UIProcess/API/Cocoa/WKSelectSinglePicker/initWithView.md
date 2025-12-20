# ``WKInternalsNotes/WKSelectSinglePicker/initWithView(_:)``

単一選択用の UIPickerView を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithView:(WKContentView *)view;
```

## Discussion
`CGRectZero` で初期化し、`WKContentView` を `_view` に保持して delegate / dataSource を自身に設定する。選択状態は `focusedSelectElementOptions` を走査して `isSelected` の項目を探し、見つかった場合は `_selectedIndex` を設定して `reloadAllComponents` のあとに該当行を選択する。

## References
- [`WKFormSelectPicker.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.h#L38)
- [`WKFormSelectPicker.mm#L358`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.mm#L358)
- [`WKFormSelectPicker.mm#L363`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.mm#L363)
- [`WKFormSelectPicker.mm#L370`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.mm#L370)
- [`WKFormSelectPicker.mm#L377`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.mm#L377)
- [`WKFormSelectPicker.mm#L379`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.mm#L379)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
