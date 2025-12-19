# ``WKInternalsNotes/WKSelectMenuListViewControllerDelegate/selectMenu(_:hasSelectedOptionAtIndex:)``

指定項目が選択されているかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)selectMenu:(WKSelectMenuListViewController *)selectMenu hasSelectedOptionAtIndex:(NSUInteger)index;
```

## Discussion
範囲外の場合は assertion を出して `NO` を返す。範囲内なら `focusedSelectElementOptions[index].isSelected` を返す。

## References
- [`WKSelectMenuListViewController.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKSelectMenuListViewController.h#L37)
- [`WKContentViewInteraction.mm#L9254`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9254)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
