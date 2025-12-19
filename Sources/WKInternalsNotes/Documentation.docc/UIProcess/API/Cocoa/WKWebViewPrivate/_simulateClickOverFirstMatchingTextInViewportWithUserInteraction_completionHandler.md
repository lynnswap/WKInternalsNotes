# ``WKInternalsNotes/WKWebView/_simulateClickOverFirstMatchingTextInViewportWithUserInteraction(_:completionHandler:)``

`_simulateClickOverFirstMatchingTextInViewportWithUserInteraction` を実行する。

## Objective-C Declaration
```objective-c
- (void)_simulateClickOverFirstMatchingTextInViewportWithUserInteraction:(NSString *)targetText completionHandler:(void(^)(BOOL))completionHandler WK_API_AVAILABLE(macos(15.2), ios(18.2), visionos(2.2));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L624`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L624)
- [`API/Cocoa/WKWebView.mm#L6320`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6320)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
