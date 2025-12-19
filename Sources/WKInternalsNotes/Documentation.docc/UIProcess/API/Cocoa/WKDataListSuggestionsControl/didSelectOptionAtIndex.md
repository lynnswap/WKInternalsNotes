# ``WKInternalsNotes/WKDataListSuggestionsControl/didSelectOptionAtIndex(_:)``

指定インデックスの候補を選択したことを通知する。

## Objective-C Declaration
```objective-c
- (void)didSelectOptionAtIndex:(NSInteger)index;
```

## Discussion
`_dropdown->didSelectOption` を通じて、候補の value を WebKit 側へ伝える。

## References
- [`WebDataListSuggestionsDropdownIOS.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.h#L47)
- [`WebDataListSuggestionsDropdownIOS.mm#L186`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.mm#L186)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
