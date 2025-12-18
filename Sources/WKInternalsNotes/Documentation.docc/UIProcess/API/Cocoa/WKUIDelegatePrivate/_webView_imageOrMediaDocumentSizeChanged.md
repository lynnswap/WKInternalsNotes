# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:imageOrMediaDocumentSizeChanged:)``

画像/メディアドキュメントのサイズ変化を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView imageOrMediaDocumentSizeChanged:(CGSize)size WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
UIClient が `WebCore::IntSize` の変化を受け取り、delegate に新しいサイズを渡す。

## References
- [`WKUIDelegatePrivate.h#L163`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L163)
- [`UIDelegate.mm#L1918`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1918)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
