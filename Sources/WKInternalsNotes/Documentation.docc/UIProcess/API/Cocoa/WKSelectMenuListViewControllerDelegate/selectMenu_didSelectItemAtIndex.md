# ``WKInternalsNotes/WKSelectMenuListViewControllerDelegate/selectMenu(_:didSelectItemAtIndex:)``

単一選択の項目選択を反映する。

## Objective-C Declaration
```objective-c
- (void)selectMenu:(WKSelectMenuListViewController *)selectMenu didSelectItemAtIndex:(NSUInteger)index;
```

## Discussion
マルチセレクトでないことを前提に、`updateFocusedElementSelectedIndex:allowsMultipleSelection:` を `false` で呼び出す。

## References
- [`WKSelectMenuListViewController.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKSelectMenuListViewController.h#L34)
- [`WKContentViewInteraction.mm#L9209`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9209)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
