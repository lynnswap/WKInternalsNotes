# ``WKInternalsNotes/_WKFindDelegate/_webView(_:didFindMatches:forString:withMatchIndex:)``

検索一致数と現在の一致インデックスを通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didFindMatches:(NSUInteger)matches forString:(NSString *)string withMatchIndex:(NSInteger)matchIndex;
```

## Discussion
`FindClient::didFindString` から delegate に転送され、`_webView:didFindMatches:forString:withMatchIndex:` を実装している場合のみ呼ばれる。`matches` は一致件数、`string` は検索文字列、`matchIndex` は現在の一致位置。

## References
- [`FindClient.mm#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/FindClient.mm#L63)
- [`_WKFindDelegate.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFindDelegate.h#L34)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
