# ``WKInternalsNotes/WKWebView/_dataTaskWithRequest(_:runAtForegroundPriority:completionHandler:)``

`_dataTaskWithRequest` を実行する。

## Objective-C Declaration
```objective-c
- (void)_dataTaskWithRequest:(NSURLRequest *)request runAtForegroundPriority:(BOOL)runAtForegroundPriority completionHandler:(void(^)(_WKDataTask *))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L521`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L521)
- [`API/Cocoa/WKWebView.mm#L4154`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4154)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
