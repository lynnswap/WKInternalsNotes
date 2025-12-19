# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:createWebViewWithConfiguration:forNavigationAction:windowFeatures:completionHandler:)``

新規 WebView の生成を非同期で delegate に依頼する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView createWebViewWithConfiguration:(WKWebViewConfiguration *)configuration forNavigationAction:(WKNavigationAction *)navigationAction windowFeatures:(WKWindowFeatures *)windowFeatures completionHandler:(void (^)(WKWebView *webView))completionHandler WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
UIClient が delegate を呼び出し、completionHandler で返された `WKWebView` を新規ページとして採用する。

## References
- [`WKUIDelegatePrivate.h#L158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L158)
- [`UIDelegate.mm#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L135)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
