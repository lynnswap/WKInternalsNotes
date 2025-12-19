# ``WKInternalsNotes/WKSelectMenuListViewControllerDelegate/selectMenu(_:displayTextForItemAtIndex:)``

指定インデックスの表示テキストを返す。

## Objective-C Declaration
```objective-c
- (NSString *)selectMenu:(WKSelectMenuListViewController *)selectMenu displayTextForItemAtIndex:(NSUInteger)index;
```

## Discussion
範囲外の場合は assertion を出して空文字列を返す。範囲内なら `focusedSelectElementOptions[index].text` を返す。

## References
- [`WKSelectMenuListViewController.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKSelectMenuListViewController.h#L39)
- [`WKContentViewInteraction.mm#L9220`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9220)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
