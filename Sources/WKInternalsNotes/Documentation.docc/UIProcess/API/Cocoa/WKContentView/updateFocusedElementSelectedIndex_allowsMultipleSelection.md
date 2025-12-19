# ``WKInternalsNotes/WKContentView/updateFocusedElementSelectedIndex(_:allowsMultipleSelection:)``

フォーカス中の選択要素で指定インデックスを選択する。

## Objective-C Declaration
```objective-c
- (void)updateFocusedElementSelectedIndex:(uint32_t)index allowsMultipleSelection:(bool)allowsMultipleSelection;
```

## Discussion
`_page->setFocusedElementSelectedIndex` にインデックスと複数選択可否を渡す。

## References
- [`WKContentViewInteraction.h#L876`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L876)
- [`WKContentViewInteraction.mm#L6254`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6254)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
