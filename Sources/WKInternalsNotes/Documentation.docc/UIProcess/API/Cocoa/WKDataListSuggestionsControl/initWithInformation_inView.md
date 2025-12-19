# ``WKInternalsNotes/WKDataListSuggestionsControl/initWithInformation(_:inView:)``

datalist 候補情報と対象ビューを指定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithInformation:(WebCore::DataListSuggestionInformation&&)information inView:(WKContentView *)view;
```

## Discussion
`view` を保持し、候補リストを `information.suggestions` から取り込む。`_setDataListSuggestionsControl:` を通じて `WKContentView` に登録する。

## References
- [`WebDataListSuggestionsDropdownIOS.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.h#L45)
- [`WebDataListSuggestionsDropdownIOS.mm#L163`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.mm#L163)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
