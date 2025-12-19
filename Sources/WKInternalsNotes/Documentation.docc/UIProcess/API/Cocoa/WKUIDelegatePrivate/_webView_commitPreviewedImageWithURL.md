# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:commitPreviewedImageWithURL:)``

画像プレビューのコミットを delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView commitPreviewedImageWithURL:(NSURL *)imageURL WK_API_DEPRECATED_WITH_REPLACEMENT("webView:contextMenuForElement:willCommitWithAnimator:", ios(9.0, 13.0));
```

## Discussion
コンテキストメニューのプレビュー確定時に、画像 URL が HTTP 系または data の場合に delegate を呼び出す。

## References
- [`WKUIDelegatePrivate.h#L227`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L227)
- [`WKContentViewInteraction.mm#L15346`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L15346)
- [`WKContentViewInteraction.mm#L15346`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L15346)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
