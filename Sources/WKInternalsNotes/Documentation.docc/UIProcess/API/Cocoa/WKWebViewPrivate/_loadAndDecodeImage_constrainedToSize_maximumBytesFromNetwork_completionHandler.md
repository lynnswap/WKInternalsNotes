# ``WKInternalsNotes/WKWebView/_loadAndDecodeImage(_:constrainedToSize:maximumBytesFromNetwork:completionHandler:)``

`_loadAndDecodeImage` を実行する。

## Objective-C Declaration
```objective-c
- (void)_loadAndDecodeImage:(NSURLRequest *)request constrainedToSize:(CGSize)maxSize maximumBytesFromNetwork:(size_t)maximumBytesFromNetwork completionHandler:(void (^)(UIImage *, NSError *))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L201`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L201)
- [`API/Cocoa/WKWebView.mm#L4639`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4639)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
