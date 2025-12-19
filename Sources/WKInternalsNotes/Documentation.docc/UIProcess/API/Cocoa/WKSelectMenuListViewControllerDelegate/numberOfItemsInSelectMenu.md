# ``WKInternalsNotes/WKSelectMenuListViewControllerDelegate/numberOfItemsInSelectMenu(_:)``

select 要素の項目数を返す。

## Objective-C Declaration
```objective-c
- (NSUInteger)numberOfItemsInSelectMenu:(WKSelectMenuListViewController *)selectMenu;
```

## Discussion
`focusedSelectElementOptions` のサイズを返す。

## References
- [`WKSelectMenuListViewController.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKSelectMenuListViewController.h#L38)
- [`WKContentViewInteraction.mm#L9215`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9215)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
