# ``WKInternalsNotes/WKWebView/_describeInteraction(_:completionHandler:)``

`_describeInteraction` を実行する。

## Objective-C Declaration
```objective-c
- (void)_describeInteraction:(_WKTextExtractionInteraction *)interaction completionHandler:(void (^)(NSString *, NSError *))completionHandler;
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewInternal.h#L685`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L685)
- [`API/Cocoa/WKWebView.mm#L6882`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6882)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
