# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:previewViewControllerForURL:defaultActions:elementInfo:)``

URL と既定アクションを渡してプレビュー用 view controller を delegate に返させる。

## Objective-C Declaration
```objective-c
- (UIViewController *)_webView:(WKWebView *)webView previewViewControllerForURL:(NSURL *)url defaultActions:(NSArray<_WKElementAction *> *)actions elementInfo:(_WKActivatedElementInfo *)elementInfo WK_API_DEPRECATED_WITH_REPLACEMENT("webView:contextMenuConfigurationForElement:completionHandler:", ios(9.0, 13.0));
```

## Discussion
WKContentViewInteraction がリンクプレビューの既定アクションと `_WKActivatedElementInfo` を作成し、旧 API として `ALLOW_DEPRECATED_DECLARATIONS` 内で呼び出す。

## References
- [`WKUIDelegatePrivate.h#L267`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L267)
- [`WKContentViewInteraction.mm#L14910`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14910)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
