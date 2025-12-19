# ``WKInternalsNotes/WKWebView/_frameInfoFromHandle(_:completionHandler:)``

`_frameInfoFromHandle` を実行する。

## Objective-C Declaration
```objective-c
- (void)_frameInfoFromHandle:(_WKFrameHandle *)handle completionHandler:(void (^)(WKFrameInfo *))completionHandler WK_API_AVAILABLE(macos(15.4), ios(18.4));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L242`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L242)
- [`API/Cocoa/WKWebView.mm#L3865`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3865)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
