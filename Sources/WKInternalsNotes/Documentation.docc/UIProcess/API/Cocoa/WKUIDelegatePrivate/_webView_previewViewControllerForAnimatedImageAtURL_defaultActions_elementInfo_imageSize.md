# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:previewViewControllerForAnimatedImageAtURL:defaultActions:elementInfo:imageSize:)``

アニメーション画像プレビュー用の view controller を delegate に返させる。

## Objective-C Declaration
```objective-c
- (UIViewController *)_webView:(WKWebView *)webView previewViewControllerForAnimatedImageAtURL:(NSURL *)url defaultActions:(NSArray<_WKElementAction *> *)actions elementInfo:(_WKActivatedElementInfo *)elementInfo imageSize:(CGSize)imageSize WK_API_DEPRECATED_WITH_REPLACEMENT("webView:contextMenuConfigurationForElement:completionHandler:", ios(9.0, 13.0));
```

## Discussion
リンクプレビュー処理中、アニメーション画像かつ URL が有効な場合に delegate へ問い合わせ、旧 API として `ALLOW_DEPRECATED_DECLARATIONS` 内で利用される。

## References
- [`WKUIDelegatePrivate.h#L268`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L268)
- [`WKContentViewInteraction.mm#L15623`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L15623)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
