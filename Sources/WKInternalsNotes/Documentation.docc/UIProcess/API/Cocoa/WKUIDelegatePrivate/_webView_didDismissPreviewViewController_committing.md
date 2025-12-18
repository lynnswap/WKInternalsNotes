# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didDismissPreviewViewController:committing:)``

プレビュー view controller の dismiss と commit 状態を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didDismissPreviewViewController:(UIViewController *)previewedViewController committing:(BOOL)committing WK_API_DEPRECATED_WITH_REPLACEMENT("webView:contextMenuDidEndForElement:", ios(9.0, 13.0));
```

## Discussion
プレビュー dismiss 時に `committing` を含めて delegate に通知する。

## References
- [`WKUIDelegatePrivate.h#L244`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L244)
- [`WKContentViewInteraction.mm#L15748`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L15748)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
