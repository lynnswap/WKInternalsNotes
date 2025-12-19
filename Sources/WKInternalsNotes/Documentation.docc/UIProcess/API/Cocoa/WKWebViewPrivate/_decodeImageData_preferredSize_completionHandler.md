# ``WKInternalsNotes/WKWebView/_decodeImageData(_:preferredSize:completionHandler:)``

`_decodeImageData` を実行する。

## Objective-C Declaration
```objective-c
- (void)_decodeImageData:(NSData *)imageData preferredSize:(NSValue *)preferredSize completionHandler:(void (^)(NSImage *, NSError *))completionHandler WK_API_AVAILABLE(macos(15.4));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L209`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L209)
- [`API/Cocoa/WKWebView.mm#L4700`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4700)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
