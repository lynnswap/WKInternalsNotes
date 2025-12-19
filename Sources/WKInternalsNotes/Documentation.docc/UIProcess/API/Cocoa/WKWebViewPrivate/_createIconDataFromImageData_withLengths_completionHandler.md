# ``WKInternalsNotes/WKWebView/_createIconDataFromImageData(_:withLengths:completionHandler:)``

`_createIconDataFromImageData` を実行する。

## Objective-C Declaration
```objective-c
- (void)_createIconDataFromImageData:(NSData *)imageData withLengths:(NSArray<NSNumber *> *)lengths completionHandler:(void (^)(NSData *, NSError *))completionHandler WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L207`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L207)
- [`WKWebView.mm#L4680`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4680)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
