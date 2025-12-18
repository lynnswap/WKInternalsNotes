# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewCanBecomeFocused(_:)``

WebView がフォーカス可能かを delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (BOOL)_webViewCanBecomeFocused:(WKWebView *)webView WK_API_AVAILABLE(ios(15.0));
```

## Discussion
WKContentView の `canBecomeFocused` で delegate が実装していれば結果を使用し、未実装時は `_webView:takeFocus:` の有無を基準にする。

## References
- [`WKUIDelegatePrivate.h#L300`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L300)
- [`WKContentView.mm#L802`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L802)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
