# ``WKInternalsNotes/WKDataListSuggestionsControl/textSuggestions()``

テキスト入力用の候補配列を返す。

## Objective-C Declaration
```objective-c
- (NSArray<WKDataListTextSuggestion *> *)textSuggestions;
```

## Discussion
最大 3 件までの候補を `WKDataListTextSuggestion` に変換して返す。

## References
- [`WebDataListSuggestionsDropdownIOS.mm#L195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.mm#L195)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
