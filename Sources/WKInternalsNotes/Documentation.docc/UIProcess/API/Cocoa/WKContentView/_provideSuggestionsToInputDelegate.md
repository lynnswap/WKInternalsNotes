# ``WKInternalsNotes/WKContentView/_provideSuggestionsToInputDelegate(_:)``

入力候補を input delegate に提供する。

## Objective-C Declaration
```objective-c
- (void)_provideSuggestionsToInputDelegate:(NSArray<WKBETextSuggestion *> *)suggestions;
```

## Discussion
BrowserEngineKit + async interactions の場合は `WKBETextSuggestion` をそのまま渡す。そうでない場合は `UITextSuggestion` に変換して `setSuggestions:` へ渡す。

## References
- [`WKContentViewInteraction.h#L801`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L801)
- [`WKContentViewInteraction.mm#L9639`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9639)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
