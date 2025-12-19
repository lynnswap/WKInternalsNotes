# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:contextMenuWillPresentForElement:)``

コンテキストメニュー表示直前を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView contextMenuWillPresentForElement:(WKContextMenuElementInfo *)elementInfo WK_API_AVAILABLE(ios(13.0));
```

## Discussion
コンテキストメニュー表示直前に delegate を呼び出す（公開 API 未実装時は private API を使用）。

## References
- [`WKUIDelegatePrivate.h#L233`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L233)
- [`WKContentViewInteraction.mm#L14788`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14788)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
