# ``WKInternalsNotes/WKWebView/_getInformationFromImageData(_:completionHandler:)``

`_getInformationFromImageData` を取得する。

## Objective-C Declaration
```objective-c
- (void)_getInformationFromImageData:(NSData *)imageData completionHandler:(void (^)(NSString *typeIdentifier, NSArray<NSValue *> *availableSizes, NSError *error))completionHandler WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L205`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L205)
- [`API/Cocoa/WKWebView.mm#L4659`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4659)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
