# ``WKInternalsNotes/WKContentView/dataListTextSuggestions``

datalist のテキスト候補配列を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong) NSArray<WKBETextSuggestion *> *dataListTextSuggestions;
```

## Default Value
未設定の場合は `nil`。

## Discussion
getter は `_dataListTextSuggestions` を返す。setter は同一配列の場合は何もせず、更新後に必要なら `updateTextSuggestionsForInputDelegate` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L537`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L537)
- [`WKContentViewInteraction.mm#L9595`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9595)
- [`WKContentViewInteraction.mm#L9611`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9611)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
