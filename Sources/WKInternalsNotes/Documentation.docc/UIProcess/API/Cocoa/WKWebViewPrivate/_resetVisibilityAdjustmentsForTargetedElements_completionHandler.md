# ``WKInternalsNotes/WKWebView/_resetVisibilityAdjustmentsForTargetedElements(_:completionHandler:)``

`_resetVisibilityAdjustmentsForTargetedElements` をリセットする。

## Objective-C Declaration
```objective-c
- (void)_resetVisibilityAdjustmentsForTargetedElements:(NSArray<_WKTargetedElementInfo *> *)elements completionHandler:(void(^)(BOOL success))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L526`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L526)
- [`API/Cocoa/WKWebView.mm#L6279`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6279)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
