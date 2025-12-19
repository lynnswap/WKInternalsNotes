# ``WKInternalsNotes/WKDataListSuggestionsControl/showSuggestionsDropdown(_:activationType:)``

dropdown への参照を設定する。

## Objective-C Declaration
```objective-c
- (void)showSuggestionsDropdown:(WebKit::WebDataListSuggestionsDropdownIOS&)dropdown activationType:(WebCore::DataListSuggestionActivationType)activationType;
```

## Discussion
`dropdown` を `_dropdown` に保存する。`activationType` は現状このメソッド内では使用しない。

## References
- [`WebDataListSuggestionsDropdownIOS.mm#L181`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.mm#L181)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
