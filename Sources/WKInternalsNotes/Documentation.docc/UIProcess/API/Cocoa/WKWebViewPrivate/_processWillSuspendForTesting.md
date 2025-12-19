# ``WKInternalsNotes/WKWebView/_processWillSuspendForTesting(_:)``

`_processWillSuspendForTesting` を実行する。

## Objective-C Declaration
```objective-c
- (void)_processWillSuspendForTesting:(void (^)(void))completionHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivateForTesting.h#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L109)
- [`WKWebViewTesting.mm#L388`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L388)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
