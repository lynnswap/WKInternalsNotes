# ``WKInternalsNotes/WKTextInputListViewControllerDelegate/shouldDisplayInputContextViewForListViewController(_:)``

入力コンテキストビューを表示するかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)shouldDisplayInputContextViewForListViewController:(PUICQuickboardViewController *)controller;
```

## Discussion
真の場合は `inputContextViewForViewController:` が使われ、偽の場合はコンテキストビューを表示しない。

## References
- [`WKTextInputListViewController.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.h#L48)
- [`WKTextInputListViewController.mm#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.mm#L71)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
