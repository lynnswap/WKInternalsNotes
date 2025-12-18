# ``WKInternalsNotes/WKUIDelegatePrivate/_contextMenuHintPreviewContainerViewForWebView(_:)``

コンテキストメニューのヒント用プレビューコンテナを返す。

## Objective-C Declaration
```objective-c
- (UIView *)_contextMenuHintPreviewContainerViewForWebView:(WKWebView *)webView WK_API_AVAILABLE(ios(15.0));
```

## Discussion
WKContentViewInteraction が delegate から返された `UIView` をコンテナとして使用し、未指定なら `_interactionViewsContainerView` を使う。

## References
- [`WKUIDelegatePrivate.h#L265`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L265)
- [`WKContentViewInteraction.mm#L10328`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10328)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
