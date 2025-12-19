# ``WKInternalsNotes/WKWebView/_adjustVisibilityForTargetedElements(_:completionHandler:)``

`_adjustVisibilityForTargetedElements` を実行する。

## Objective-C Declaration
```objective-c
- (void)_adjustVisibilityForTargetedElements:(NSArray<_WKTargetedElementInfo *> *)elements completionHandler:(void(^)(BOOL success))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L523`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L523)
- [`WKWebView.mm#L6286`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6286)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
