# ``WKInternalsNotes/WKDataListSuggestionsControl/suggestionLabelAtIndex(_:)``

指定インデックスの候補ラベルを返す。

## Objective-C Declaration
```objective-c
- (String)suggestionLabelAtIndex:(NSInteger)index;
```

## Discussion
`_suggestions[index].label` を返す。

## References
- [`WebDataListSuggestionsDropdownIOS.mm#L218`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.mm#L218)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
