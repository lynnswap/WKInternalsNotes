# ``WKInternalsNotes/WKContentView/_accessibilityClearSelection()``

アクセシビリティ向けに保存している選択状態を解除する。

## Objective-C Declaration
```objective-c
- (void)_accessibilityClearSelection;
```

## Discussion
`_page->storeSelectionForAccessibility(false)` を呼び、アクセシビリティ用の選択状態をクリアする。

## References
- [WKContentViewInteraction.h#L854](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L854)
- [WKContentViewInteraction.mm#L5106](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L5106)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
