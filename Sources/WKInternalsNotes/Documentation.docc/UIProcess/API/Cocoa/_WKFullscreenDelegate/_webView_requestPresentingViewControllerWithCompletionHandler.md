# ``WKInternalsNotes/_WKFullscreenDelegate/_webView(_:requestPresentingViewControllerWithCompletionHandler:)``

表示用の `UIViewController` を要求する（iOS）。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView requestPresentingViewControllerWithCompletionHandler:(void (^)(UIViewController * _Nullable, NSError * _Nullable))completionHandler;
```

## Discussion
`FullscreenClient::requestPresentingViewController` から呼び出され、未実装の場合は `completionHandler(nil, nil)` が実行される。

## References
- [`_WKFullscreenDelegate.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFullscreenDelegate.h#L44)
- [`FullscreenClient.mm#L143`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/FullscreenClient.mm#L143)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
