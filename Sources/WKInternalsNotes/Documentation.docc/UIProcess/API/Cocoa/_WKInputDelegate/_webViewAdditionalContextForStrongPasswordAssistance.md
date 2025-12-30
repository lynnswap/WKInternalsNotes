# ``WKInternalsNotes/_WKInputDelegate/_webViewAdditionalContextForStrongPasswordAssistance(_:)``

強力パスワード支援用の追加コンテキストを返す。

## Objective-C Declaration
```objective-c
- (NSDictionary<id, NSString *> *)_webViewAdditionalContextForStrongPasswordAssistance:(WKWebView *)webView WK_API_AVAILABLE(ios(13.4));
```

## Discussion
`WKContentViewInteraction` の `_continueElementDidFocus` で、delegate が実装していれば呼ばれる。戻り値は `_additionalContextForStrongPasswordAssistance` に保持され、未実装時は空の辞書を使用する。

## References
- [`_WKInputDelegate.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInputDelegate.h#L61)
- [`WKContentViewInteraction.mm#L8504`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8504)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
