# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:contextMenu:forElement:userInfo:)``

userInfo 付きでコンテキストメニューを delegate が調整する。

## Objective-C Declaration
```objective-c
- (NSMenu *)_webView:(WKWebView *)webView contextMenu:(NSMenu *)menu forElement:(_WKContextMenuElementInfo *)element userInfo:(id <NSSecureCoding>)userInfo WK_API_DEPRECATED_WITH_REPLACEMENT("_webView:getContextMenuFromProposedMenu:forElement:userInfo:completionHandler:", macos(10.12, 10.14.4));
```

## Discussion
`contextMenu:forElement:` 未実装時に `contextMenu:forElement:userInfo:` を呼び出し、返った `NSMenu` を使用する。

## References
- [`WKUIDelegatePrivate.h#L333`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L333)
- [`UIDelegate.mm#L307`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L307)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
