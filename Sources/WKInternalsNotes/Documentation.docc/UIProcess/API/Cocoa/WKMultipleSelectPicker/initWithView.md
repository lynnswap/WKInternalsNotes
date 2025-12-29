# ``WKInternalsNotes/WKMultipleSelectPicker/initWithView(_:)``

複数選択ピッカーを `WKContentView` から初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithView:(WKContentView *)view;
```

## Discussion
`focusedElementInformation.isMultiSelect` に基づいて複数選択可否を設定し、`dataSource`/`delegate` を自分に設定する。フレームサイズを `sizeForLegacyFormControlPickerViews` に合わせて再読み込みし、単一選択時は最初に選択済みの行を選択する。

## References
- [`WKFormSelectPicker.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.h#L38)
- [`WKFormSelectPicker.mm#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.mm#L150)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
