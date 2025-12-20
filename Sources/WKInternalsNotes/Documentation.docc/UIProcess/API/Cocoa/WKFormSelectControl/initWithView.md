# ``WKInternalsNotes/WKFormSelectControl/initWithView(_:)``

セレクトフォーム用の入力コントロールを構成して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithView:(WKContentView *)view;
```

## Discussion
`focusedElementInformation.selectOptions` からグループ有無を判定し、`_shouldUseContextMenusForFormControls` の場合は `WKSelectPicker` / `WKSelectMultiplePicker` を選ぶ。コンテキストメニューを使わない場合は、画面サイズや `isMultiSelect` / `hasGroups` に応じて `WKSelectPopover` / `WKMultipleSelectPicker` / `WKSelectSinglePicker` を生成し、`super initWithView:control:` に渡して初期化する。

## References
- [`WKFormSelectControl.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.h#L39)
- [`WKFormSelectControl.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.mm#L66)
- [`WKFormSelectControl.mm#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.mm#L78)
- [`WKFormSelectControl.mm#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.mm#L88)
- [`WKFormSelectControl.mm#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.mm#L95)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
