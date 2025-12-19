# ``WKInternalsNotes/WKWebView/_setSystemPreviewCompletionHandlerForLoadTesting(_:)``

`_setSystemPreviewCompletionHandlerForLoadTesting` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setSystemPreviewCompletionHandlerForLoadTesting:(void(^)(bool))completionHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L149)
- [`API/Cocoa/WKWebViewTesting.mm#L725`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L725)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
