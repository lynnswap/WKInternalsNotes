# ``WKInternalsNotes/WKTextInputListViewControllerDelegate/textInputContextForListViewController(_:)``

テキスト入力コンテキストを返す。

## Objective-C Declaration
```objective-c
- (PUICTextInputContext *)textInputContextForListViewController:(WKTextInputListViewController *)controller;
```

## Discussion
`initWithDelegate:` 内で `textInputContext` に設定される。

## References
- [`WKTextInputListViewController.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.h#L44)
- [`WKTextInputListViewController.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.mm#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
