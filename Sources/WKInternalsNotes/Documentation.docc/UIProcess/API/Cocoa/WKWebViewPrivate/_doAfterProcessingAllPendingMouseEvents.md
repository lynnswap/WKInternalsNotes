# ``WKInternalsNotes/WKWebView/_doAfterProcessingAllPendingMouseEvents(_:)``

`_doAfterProcessingAllPendingMouseEvents` を実行する。

## Objective-C Declaration
```objective-c
- (void)_doAfterProcessingAllPendingMouseEvents:(dispatch_block_t)action;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivateForTesting.h#L116`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L116)
- [`WKWebViewTesting.mm#L481`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L481)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
