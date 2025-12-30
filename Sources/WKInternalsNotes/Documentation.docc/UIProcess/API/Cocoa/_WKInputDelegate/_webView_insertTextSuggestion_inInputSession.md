# ``WKInternalsNotes/_WKInputDelegate/_webView(_:insertTextSuggestion:inInputSession:)``

テキスト候補の挿入を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView insertTextSuggestion:(UITextSuggestion *)suggestion inInputSession:(id <_WKFormInputSession>)inputSession WK_API_AVAILABLE(ios(10.0));
```

## Discussion
`WKContentViewInteraction` の `insertTextSuggestion:` 内で、オートフィルやデータリスト処理の後に delegate が実装していれば呼ばれる。`BETextSuggestion` は UIKit の `UITextSuggestion` に変換して渡す。

## References
- [`_WKInputDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInputDelegate.h#L48)
- [`WKContentViewInteraction.mm#L6460`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6460)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
