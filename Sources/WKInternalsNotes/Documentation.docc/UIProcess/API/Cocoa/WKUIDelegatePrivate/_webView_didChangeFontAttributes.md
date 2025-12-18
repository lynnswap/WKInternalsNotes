# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didChangeFontAttributes:)``

フォント属性の変更を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didChangeFontAttributes:(NSDictionary<NSString *, id> *)fontAttributes WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
`WebCore::FontAttributes` を辞書に変換して delegate に渡す。

## References
- [`WKUIDelegatePrivate.h#L189`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L189)
- [`UIDelegate.mm#L1298`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1298)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
