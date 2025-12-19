# ``WKInternalsNotes/WKSelectMenuListViewControllerDelegate/selectMenuUsesMultipleSelection(_:)``

複数選択モードかどうかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)selectMenuUsesMultipleSelection:(WKSelectMenuListViewController *)selectMenu;
```

## Discussion
`_focusedElementInformation.isMultiSelect` を返す。

## References
- [`WKSelectMenuListViewController.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKSelectMenuListViewController.h#L40)
- [`WKContentViewInteraction.mm#L9249`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9249)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
