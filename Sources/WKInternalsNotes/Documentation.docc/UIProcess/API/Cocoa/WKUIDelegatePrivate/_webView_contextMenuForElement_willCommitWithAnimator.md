# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:contextMenuForElement:willCommitWithAnimator:)``

コンテキストメニューの commit を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView contextMenuForElement:(WKContextMenuElementInfo *)elementInfo willCommitWithAnimator:(id<UIContextMenuInteractionCommitAnimating>)animator WK_API_AVAILABLE(ios(13.0));
```

## Discussion
コンテキストメニューのプレビュー確定時に delegate を呼び出し、`UIContextMenuInteractionCommitAnimating` を渡す。

## References
- [`WKUIDelegatePrivate.h#L252`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L252)
- [`WKContentViewInteraction.mm#L15380`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L15380)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
