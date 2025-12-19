# ``WKInternalsNotes/WKDataListSuggestionsControl/view``

候補 UI の関連 `WKContentView` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) WKContentView *view;
```

## Default Value
`initWithInformation:inView:` で設定され、それ以前は `nil`。

## Discussion
初期化時に保持した `WKContentView` を参照する。

## References
- [`WebDataListSuggestionsDropdownIOS.mm#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.mm#L47)
- [`WebDataListSuggestionsDropdownIOS.mm#L163`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDataListSuggestionsDropdownIOS.mm#L163)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
