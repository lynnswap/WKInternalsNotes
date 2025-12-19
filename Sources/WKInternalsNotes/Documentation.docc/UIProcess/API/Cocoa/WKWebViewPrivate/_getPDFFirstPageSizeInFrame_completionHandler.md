# ``WKInternalsNotes/WKWebView/_getPDFFirstPageSizeInFrame(_:completionHandler:)``

`_getPDFFirstPageSizeInFrame` を取得する。

## Objective-C Declaration
```objective-c
- (void)_getPDFFirstPageSizeInFrame:(_WKFrameHandle *)frame completionHandler:(void(^)(CGSize))completionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L457`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L457)
- [`WKWebView.mm#L4955`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4955)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
