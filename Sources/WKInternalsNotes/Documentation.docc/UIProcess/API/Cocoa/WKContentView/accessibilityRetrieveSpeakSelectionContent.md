# ``WKInternalsNotes/WKContentView/accessibilityRetrieveSpeakSelectionContent()``

Speak Selection 用の文字列を取得して通知する。

## Objective-C Declaration
```objective-c
- (void)accessibilityRetrieveSpeakSelectionContent;
```

## Discussion
選択または内容文字列を Web プロセスから取得し、`WKWebView` の `_accessibilityDidGetSpeakSelectionContent` に渡す。`accessibilitySpeakSelectionSetContent:` を実装していれば同じ文字列を通知する。

## References
- [`WKContentViewInteraction.h#L849`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L849)
- [`WKContentViewInteraction.mm#L5064`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L5064)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
