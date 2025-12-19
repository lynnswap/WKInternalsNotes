# ``WKInternalsNotes/WKWebView/_computePagesForPrinting(_:completionHandler:)``

`_computePagesForPrinting` を実行する。

## Objective-C Declaration
```objective-c
- (void)_computePagesForPrinting:(_WKFrameHandle *)handle completionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivateForTesting.h#L145`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L145)
- [`WKWebViewTesting.mm#L697`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L697)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
