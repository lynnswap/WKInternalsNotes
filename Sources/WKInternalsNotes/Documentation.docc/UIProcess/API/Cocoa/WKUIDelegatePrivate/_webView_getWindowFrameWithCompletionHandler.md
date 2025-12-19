# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:getWindowFrameWithCompletionHandler:)``

WebView のウィンドウフレーム取得を delegate に依頼する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView getWindowFrameWithCompletionHandler:(void (^)(CGRect))completionHandler WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
UIDelegate::UIClient が `CompletionHandlerCallChecker` を伴って delegate に問い合わせ、未実装時は空の `CGRect` を返す。

## References
- [`WKUIDelegatePrivate.h#L321`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L321)
- [`UIDelegate.mm#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L139)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
