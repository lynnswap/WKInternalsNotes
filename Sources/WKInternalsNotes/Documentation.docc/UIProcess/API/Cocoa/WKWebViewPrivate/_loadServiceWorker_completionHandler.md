# ``WKInternalsNotes/WKWebView/_loadServiceWorker(_:completionHandler:)``

`_loadServiceWorker` を実行する。

## Objective-C Declaration
```objective-c
- (void)_loadServiceWorker:(NSURL *)url completionHandler:(void (^)(BOOL success))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L513`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L513)
- [`API/Cocoa/WKWebView.mm#L4727`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4727)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
