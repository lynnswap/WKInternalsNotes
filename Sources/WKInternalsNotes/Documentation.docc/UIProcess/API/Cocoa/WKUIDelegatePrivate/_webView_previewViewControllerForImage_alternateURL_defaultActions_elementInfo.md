# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:previewViewControllerForImage:alternateURL:defaultActions:elementInfo:)``

画像プレビュー用の view controller を delegate に返させる。

## Objective-C Declaration
```objective-c
- (UIViewController *)_webView:(WKWebView *)webView previewViewControllerForImage:(UIImage *)image alternateURL:(NSURL *)url defaultActions:(NSArray<_WKElementAction *> *)actions elementInfo:(_WKActivatedElementInfo *)elementInfo WK_API_DEPRECATED_WITH_REPLACEMENT("webView:contextMenuConfigurationForElement:completionHandler:", ios(11.0, 13.0));
```

## Discussion
WKContentViewInteraction が画像プレビュー処理で default actions と elementInfo を渡し、delegate が応答すればその view controller を採用する。未実装時は `WKImagePreviewViewController` を生成して代替する。

## References
- [`WKUIDelegatePrivate.h#L250`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L250)
- [`WKContentViewInteraction.mm#L14788`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14788)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
