# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:contextMenuConfigurationForElement:completionHandler:)``

コンテキストメニュー設定を非同期に delegate へ問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView contextMenuConfigurationForElement:(WKContextMenuElementInfo *)elementInfo completionHandler:(void(^)(UIContextMenuConfiguration *))completionHandler WK_API_AVAILABLE(ios(13.0));
```

## Discussion
WKContentViewInteraction が `CompletionHandlerCallChecker` を使って delegate を呼び出し、返された `UIContextMenuConfiguration` を採用する。

## References
- [`WKUIDelegatePrivate.h#L217`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L217)
- [`WKContentViewInteraction.mm#L14788`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14788)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
