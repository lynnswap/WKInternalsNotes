# ``WKInternalsNotes/WKTextInputListViewControllerDelegate/numericInputModeForListViewController(_:)``

数値入力モードを返す。

## Objective-C Declaration
```objective-c
- (WKNumberPadInputMode)numericInputModeForListViewController:(WKTextInputListViewController *)controller;
```

## Discussion
`requiresNumericInput` の判定や番号入力シートの表示時に参照され、`WKNumberPadInputModeNone` 以外が返ると数値入力が有効になる。

## References
- [`WKTextInputListViewController.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.h#L43)
- [`WKTextInputListViewController.mm#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.mm#L79)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
