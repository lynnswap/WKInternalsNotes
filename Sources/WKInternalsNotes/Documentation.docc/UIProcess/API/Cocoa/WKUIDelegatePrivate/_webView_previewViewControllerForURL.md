# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:previewViewControllerForURL:)``

URL のプレビュー用 view controller を delegate に返させる。

## Objective-C Declaration
```objective-c
- (UIViewController *)_webView:(WKWebView *)webView previewViewControllerForURL:(NSURL *)url WK_API_DEPRECATED_WITH_REPLACEMENT("webView:contextMenuConfigurationForElement:completionHandler:", ios(9.0, 13.0));
```

## Discussion
リンクプレビュー生成で `previewViewControllerForURL:defaultActions:elementInfo:` が使えない場合のフォールバックとして呼び出される。

## References
- [`WKUIDelegatePrivate.h#L241`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L241)
- [`WKContentViewInteraction.mm#L14912`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14912)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
