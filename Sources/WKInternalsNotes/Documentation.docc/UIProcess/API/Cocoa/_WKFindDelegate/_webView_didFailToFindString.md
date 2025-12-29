# ``WKInternalsNotes/_WKFindDelegate/_webView(_:didFailToFindString:)``

検索文字列が見つからなかったことを通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didFailToFindString:(NSString *)string;
```

## Discussion
`FindClient::didFailToFindString` から delegate に転送され、`_webView:didFailToFindString:` を実装している場合のみ呼ばれる。`string` は検索文字列。

## References
- [`FindClient.mm#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/FindClient.mm#L68)
- [`_WKFindDelegate.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFindDelegate.h#L34)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
