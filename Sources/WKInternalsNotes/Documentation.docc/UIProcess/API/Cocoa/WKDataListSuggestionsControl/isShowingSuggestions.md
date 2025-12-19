# ``WKInternalsNotes/WKDataListSuggestionsControl/isShowingSuggestions``

候補 UI が表示中かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isShowingSuggestions;
```

## Default Value
初期は `NO`。

## Discussion
dropdown の表示/非表示に合わせて `YES/NO` が更新される。

## References
- [`WebDataListSuggestionsDropdownIOS.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.h#L43)
- [`WebDataListSuggestionsDropdownIOS.mm#L568`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.mm#L568)
- [`WebDataListSuggestionsDropdownIOS.mm#L575`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.mm#L575)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
