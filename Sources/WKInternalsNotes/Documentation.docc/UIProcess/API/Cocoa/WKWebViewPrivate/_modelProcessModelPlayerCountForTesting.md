# ``WKInternalsNotes/WKWebView/_modelProcessModelPlayerCountForTesting(_:)``

`_modelProcessModelPlayerCountForTesting` を実行する。

## Objective-C Declaration
```objective-c
- (void)_modelProcessModelPlayerCountForTesting:(void(^)(NSUInteger))completionHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivateForTesting.h#L178`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L178)
- [`WKWebViewTesting.mm#L1092`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L1092)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
