# ``WKInternalsNotes/WKTextInputListViewControllerDelegate/allowsLanguageSelectionForListViewController(_:)``

言語選択ボタンの表示可否を返す。

## Objective-C Declaration
```objective-c
- (BOOL)allowsLanguageSelectionForListViewController:(WKTextInputListViewController *)controller;
```

## Discussion
`shouldShowLanguageButton` 内で参照される。

## References
- [`WKTextInputListViewController.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.h#L47)
- [`WKTextInputListViewController.mm#L155`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.mm#L155)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
