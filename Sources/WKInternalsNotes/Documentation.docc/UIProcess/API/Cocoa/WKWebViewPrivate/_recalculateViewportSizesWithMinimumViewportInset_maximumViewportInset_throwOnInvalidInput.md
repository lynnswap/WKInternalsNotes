# ``WKInternalsNotes/WKWebView/_recalculateViewportSizesWithMinimumViewportInset(_:maximumViewportInset:throwOnInvalidInput:)``

`_recalculateViewportSizesWithMinimumViewportInset` を実行する。

## Objective-C Declaration
```objective-c
- (void)_recalculateViewportSizesWithMinimumViewportInset:(CocoaEdgeInsets)minimumViewportInset maximumViewportInset:(CocoaEdgeInsets)maximumViewportInset throwOnInvalidInput:(BOOL)throwOnInvalidInput;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewInternal.h#L555`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L555)
- [`WKWebView.mm#L2004`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L2004)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
