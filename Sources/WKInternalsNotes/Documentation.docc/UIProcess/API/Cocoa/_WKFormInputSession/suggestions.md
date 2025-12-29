# ``WKInternalsNotes/_WKFormInputSession/suggestions``

テキスト入力の候補一覧を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSArray<UITextSuggestion *> *suggestions WK_API_AVAILABLE(ios(10.0));
```

## Default Value
`nil`。

## Discussion
setter で変更があれば `copy` して保持し、`updateTextSuggestionsForInputDelegate` を呼ぶ。getter は保持している配列を返す。

## References
- [`WKContentViewInteraction.mm#L879`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L879)
- [`WKContentViewInteraction.mm#L884`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L884)
- [`_WKFormInputSession.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFormInputSession.h#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
