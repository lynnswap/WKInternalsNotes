# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:printFrame:pdfFirstPageSize:completionHandler:)``

PDF 1ページ目サイズを含めて印刷処理を delegate に依頼する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView printFrame:(_WKFrameHandle *)frame pdfFirstPageSize:(CGSize)size completionHandler:(void (^)(void))completionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
UIDelegate::UIClient が `CompletionHandlerCallChecker` を使って delegate へ依頼し、完了時に `completionHandler` を呼ぶ。

## References
- [`WKUIDelegatePrivate.h#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L141)
- [`UIDelegate.mm#L159`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L159)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
