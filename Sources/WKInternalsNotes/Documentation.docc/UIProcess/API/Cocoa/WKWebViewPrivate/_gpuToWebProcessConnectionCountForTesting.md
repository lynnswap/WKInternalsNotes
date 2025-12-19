# ``WKInternalsNotes/WKWebView/_gpuToWebProcessConnectionCountForTesting(_:)``

`_gpuToWebProcessConnectionCountForTesting` を実行する。

## Objective-C Declaration
```objective-c
- (void)_gpuToWebProcessConnectionCountForTesting:(void(^)(NSUInteger))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L141)
- [`API/Cocoa/WKWebViewTesting.mm#L705`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L705)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
