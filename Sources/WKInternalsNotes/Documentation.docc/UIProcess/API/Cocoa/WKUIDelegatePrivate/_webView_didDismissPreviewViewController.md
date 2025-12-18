# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didDismissPreviewViewController:)``

プレビュー view controller の dismiss を通知する（旧 API）。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didDismissPreviewViewController:(UIViewController *)previewedViewController WK_API_DEPRECATED_WITH_REPLACEMENT("webView:contextMenuDidEndForElement:", ios(9.0, 13.0));
```

## Discussion
`didDismissPreviewViewController:committing:` 未実装時にこちらを呼び出す。

## References
- [`WKUIDelegatePrivate.h#L245`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L245)
- [`WKContentViewInteraction.mm#L15750`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L15750)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
