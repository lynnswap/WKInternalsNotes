# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:shouldAllowPDFAtURL:toOpenFromFrame:completionHandler:)``

PDF を開く許可を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView shouldAllowPDFAtURL:(NSURL *)fileURL toOpenFromFrame:(WKFrameInfo *)frame completionHandler:(void (^)(BOOL))completionHandler WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
UIDelegate::UIClient が `CompletionHandlerCallChecker` を使い、ファイル URL と `WKFrameInfo` を渡して許可可否を取得する。

## References
- [`WKUIDelegatePrivate.h#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L141)
- [`UIDelegate.mm#L202`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L202)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
