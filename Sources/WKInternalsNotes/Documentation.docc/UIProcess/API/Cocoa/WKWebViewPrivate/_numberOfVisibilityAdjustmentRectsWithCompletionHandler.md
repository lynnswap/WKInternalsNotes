# ``WKInternalsNotes/WKWebView/_numberOfVisibilityAdjustmentRectsWithCompletionHandler(_:)``

`_numberOfVisibilityAdjustmentRectsWithCompletionHandler` を実行する。

## Objective-C Declaration
```objective-c
- (void)_numberOfVisibilityAdjustmentRectsWithCompletionHandler:(void(^)(NSUInteger))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L524`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L524)
- [`WKWebView.mm#L6293`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6293)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
