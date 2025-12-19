# ``WKInternalsNotes/WKContentView/_selectDataListOption(_:)``

datalist の指定候補を選択する。

## Objective-C Declaration
```objective-c
- (void)_selectDataListOption:(NSInteger)optionIndex;
```

## Discussion
`_dataListSuggestionsControl` に `didSelectOptionAtIndex:` を渡す。

## References
- [`WKContentViewInteraction.h#L1056`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1056)
- [`WKContentViewInteraction.mm#L14692`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14692)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
