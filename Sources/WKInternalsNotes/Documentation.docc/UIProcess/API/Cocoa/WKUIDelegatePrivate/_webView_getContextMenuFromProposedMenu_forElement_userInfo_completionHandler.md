# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:getContextMenuFromProposedMenu:forElement:userInfo:completionHandler:)``

提案されたコンテキストメニューを delegate に差し替えさせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView getContextMenuFromProposedMenu:(NSMenu *)menu forElement:(_WKContextMenuElementInfo *)element userInfo:(id <NSSecureCoding>)userInfo completionHandler:(void (^)(NSMenu *))completionHandler WK_API_AVAILABLE(macos(10.14));
```

## Discussion
UIDelegate が `CompletionHandlerCallChecker` を使って delegate に非同期メニュー生成を依頼し、完了後に `completionHandler` を呼び出す。未実装時は旧 `contextMenu:forElement:` 系へフォールバックする。

## References
- [`WKUIDelegatePrivate.h#L321`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L321)
- [`UIDelegate.mm#L191`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L191)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
