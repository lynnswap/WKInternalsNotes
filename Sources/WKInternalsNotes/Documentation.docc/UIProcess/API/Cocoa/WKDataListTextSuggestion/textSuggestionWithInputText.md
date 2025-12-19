# ``WKInternalsNotes/WKDataListTextSuggestion/textSuggestionWithInputText(_:)``

入力テキストから候補を生成する。

## Objective-C Declaration
```objective-c
+ (instancetype)textSuggestionWithInputText:(NSString *)inputText;
```

## Discussion
`USE(BROWSERENGINEKIT)` の場合は `initWithInputText:` を使って生成し、それ以外は `super` の実装にフォールバックする。

## References
- [`WebDataListSuggestionsDropdownIOS.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.h#L38)
- [`WebDataListSuggestionsDropdownIOS.mm#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.mm#L85)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
