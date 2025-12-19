# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:contextMenu:forElement:)``

コンテキストメニューを delegate が調整する（旧 API）。

## Objective-C Declaration
```objective-c
- (NSMenu *)_webView:(WKWebView *)webView contextMenu:(NSMenu *)menu forElement:(_WKContextMenuElementInfo *)element WK_API_DEPRECATED_WITH_REPLACEMENT("_webView:getContextMenuFromProposedMenu:forElement:userInfo:completionHandler:", macos(10.12, 10.14.4));
```

## Discussion
ContextMenuClient が `contextMenu:forElement:` を呼び出し、delegate が返した `NSMenu` を採用する。

## References
- [`WKUIDelegatePrivate.h#L321`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L321)
- [`UIDelegate.mm#L189`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L189)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
