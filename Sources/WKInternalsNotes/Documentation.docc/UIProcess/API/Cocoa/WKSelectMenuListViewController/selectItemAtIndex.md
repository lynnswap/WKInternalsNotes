# ``WKInternalsNotes/WKSelectMenuListViewController/selectItemAtIndex(_:)``

指定インデックスの項目を選択する。

## Objective-C Declaration
```objective-c
- (void)selectItemAtIndex:(NSInteger)index;
```

## Discussion
`HAVE(QUICKBOARD_COLLECTION_VIEWS)` に応じて section を決め、`didSelectListItemAtIndexPath:` を呼ぶ。

## References
- [`WKSelectMenuListViewController.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKSelectMenuListViewController.h#L56)
- [`WKSelectMenuListViewController.mm#L267`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKSelectMenuListViewController.mm#L267)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
