# ``WKInternalsNotes/WKContentView/updateTextSuggestionsForInputDelegate()``

入力候補の提示内容を input delegate に反映する。

## Objective-C Declaration
```objective-c
- (void)updateTextSuggestionsForInputDelegate;
```

## Discussion
`_formInputSession` の suggestions があればそれを優先して提供し、次に datalist の候補を使う。どちらも無い場合は `nil` を渡して候補をクリアする。

## References
- [`WKContentViewInteraction.h#L912`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L912)
- [`WKContentViewInteraction.mm#L9622`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9622)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
