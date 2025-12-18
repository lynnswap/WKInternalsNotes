# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewClose(_:)``

WebView のクローズを delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewClose:(WKWebView *)webView;
```

## Discussion
UIDelegate::UIClient の `close` で `webViewClose` が有効な場合に delegate へ通知し、処理を委ねる。

## References
- [`WKUIDelegatePrivate.h#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L149)
- [`UIDelegate.mm#L1539`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1539)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
