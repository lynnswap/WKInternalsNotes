# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:contextMenuContentPreviewForElement:)``

コンテキストメニューのプレビュー view controller を delegate が返す。

## Objective-C Declaration
```objective-c
- (UIViewController *)_webView:(WKWebView *)webView contextMenuContentPreviewForElement:(WKContextMenuElementInfo *)elementInfo WK_API_AVAILABLE(ios(15.0));
```

## Discussion
delegate が実装していればその戻り値を使い、`nil` の場合は `WKImagePreviewViewController` にフォールバックする。

## References
- [`WKUIDelegatePrivate.h#L233`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L233)
- [`WKContentViewInteraction.mm#L15175`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L15175)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
