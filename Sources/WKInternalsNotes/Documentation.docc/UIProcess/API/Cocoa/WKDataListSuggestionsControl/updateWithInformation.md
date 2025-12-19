# ``WKInternalsNotes/WKDataListSuggestionsControl/updateWithInformation(_:)``

候補情報を更新する。

## Objective-C Declaration
```objective-c
- (void)updateWithInformation:(WebCore::DataListSuggestionInformation&&)information;
```

## Discussion
`information.suggestions` を新しい候補リストとして保存する。

## References
- [`WebDataListSuggestionsDropdownIOS.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.h#L46)
- [`WebDataListSuggestionsDropdownIOS.mm#L176`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.mm#L176)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
