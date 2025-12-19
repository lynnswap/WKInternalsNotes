# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:commitPreviewedViewController:)``

プレビュー用 view controller のコミットを delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView commitPreviewedViewController:(UIViewController *)previewedViewController WK_API_DEPRECATED_WITH_REPLACEMENT("webView:contextMenuForElement:willCommitWithAnimator:", ios(9.0, 13.0));
```

## Discussion
コンテキストメニューのプレビュー確定時に `_contextMenuLegacyPreviewController` を delegate へ渡す。

## References
- [`WKUIDelegatePrivate.h#L219`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L219)
- [`WKContentViewInteraction.mm#L15346`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L15346)
- [`WKContentViewInteraction.mm#L15346`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L15346)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
