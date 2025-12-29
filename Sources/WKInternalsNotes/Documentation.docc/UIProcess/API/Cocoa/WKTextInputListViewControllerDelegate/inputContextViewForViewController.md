# ``WKInternalsNotes/WKTextInputListViewControllerDelegate/inputContextViewForViewController(_:)``

入力コンテキスト表示用のビューを返す。

## Objective-C Declaration
```objective-c
- (UIView *)inputContextViewForViewController:(PUICQuickboardViewController *)controller;
```

## Discussion
`shouldDisplayInputContextViewForListViewController:` が真のときに呼ばれ、ヘッダ用のコンテキストビューとして使われる。

## References
- [`WKTextInputListViewController.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.h#L45)
- [`WKTextInputListViewController.mm#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.mm#L71)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
