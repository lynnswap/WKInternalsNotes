# ``WKInternalsNotes/WKWebView/_dataTaskWithRequest(_:completionHandler:)``

`_dataTaskWithRequest` を実行する。

## Objective-C Declaration
```objective-c
- (void)_dataTaskWithRequest:(NSURLRequest *)request completionHandler:(void(^)(_WKDataTask *))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L520`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L520)
- [`WKWebView.mm#L4154`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4154)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
