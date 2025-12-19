# ``WKInternalsNotes/WKContentView/_accessibilityStoreSelection()``

アクセシビリティ用に選択状態を保存する。

## Objective-C Declaration
```objective-c
- (void)_accessibilityStoreSelection;
```

## Discussion
`_page->storeSelectionForAccessibility(true)` を呼び、アクセシビリティ向けの選択情報を保持する。

## References
- [WKContentViewInteraction.h#L853](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L853)
- [WKContentViewInteraction.mm#L5101](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L5101)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
