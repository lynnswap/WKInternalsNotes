# ``WKInternalsNotes/WKSelectMenuListViewControllerDelegate/selectMenu(_:didCheckItemAtIndex:checked:)``

複数選択のチェック状態を更新する。

## Objective-C Declaration
```objective-c
- (void)selectMenu:(WKSelectMenuListViewController *)selectMenu didCheckItemAtIndex:(NSUInteger)index checked:(BOOL)checked;
```

## Discussion
マルチセレクト前提で、範囲外や状態が変わらない場合は assertion で終了する。状態が変わる場合は `updateFocusedElementSelectedIndex:allowsMultipleSelection:true` を呼び、オプションの `isSelected` を更新する。

## References
- [`WKSelectMenuListViewController.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKSelectMenuListViewController.h#L35)
- [`WKContentViewInteraction.mm#L9231`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9231)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
