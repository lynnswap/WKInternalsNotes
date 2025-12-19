# ``WKInternalsNotes/WKContentView/isShowingDataListSuggestions``

データリスト候補が表示中かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isShowingDataListSuggestions;
```

## Default Value
`_dataListSuggestionsControl` の `isShowingSuggestions` を返す（未設定なら `NO`）。

## Discussion
`WKDataListSuggestionsControl` が保持する表示状態をそのまま返す。

## References
- [`WKContentViewInteraction.h#L1059`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1059)
- [`WKContentViewInteraction.mm#L14702`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14702)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
