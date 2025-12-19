# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:willPreviewImageWithURL:)``

画像プレビュー開始前を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView willPreviewImageWithURL:(NSURL *)imageURL WK_API_DEPRECATED_WITH_REPLACEMENT("webView:contextMenuConfigurationForElement:completionHandler:", ios(9.0, 13.0));
```

## Discussion
WKContentViewInteraction が画像プレビューの準備時に URL を渡して通知する（旧 API 経由）。

## References
- [`WKUIDelegatePrivate.h#L219`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L219)
- [`WKContentViewInteraction.mm#L14940`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14940)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
