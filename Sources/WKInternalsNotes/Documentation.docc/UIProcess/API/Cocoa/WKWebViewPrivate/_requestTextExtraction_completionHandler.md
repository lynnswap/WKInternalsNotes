# ``WKInternalsNotes/WKWebView/_requestTextExtraction(_:completionHandler:)``

`_requestTextExtraction` を取得する。

## Objective-C Declaration
```objective-c
- (void)_requestTextExtraction:(_WKTextExtractionConfiguration *)configuration completionHandler:(void (^)(WKTextExtractionResult *))completionHandler;
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewInternal.h#L684`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L684)
- [`WKWebView.mm#L6858`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6858)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
