# ``WKInternalsNotes/WKDataListSuggestionsControl/suggestionAtIndex(_:)``

指定インデックスの候補値を返す。

## Objective-C Declaration
```objective-c
- (String)suggestionAtIndex:(NSInteger)index;
```

## Discussion
`_suggestions[index].value` を返す。

## References
- [`WebDataListSuggestionsDropdownIOS.mm#L213`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.mm#L213)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
