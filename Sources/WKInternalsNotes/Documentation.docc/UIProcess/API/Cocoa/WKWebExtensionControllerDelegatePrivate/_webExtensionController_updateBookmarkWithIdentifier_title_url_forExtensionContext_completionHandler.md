# ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate/_webExtensionController(_:updateBookmarkWithIdentifier:title:url:forExtensionContext:completionHandler:)``

既存ブックマークの更新を要求する。

## Objective-C Declaration
```objective-c
- (void)_webExtensionController:(WKWebExtensionController *)controller updateBookmarkWithIdentifier:(NSString *)bookmarkId title:(nullable NSString *)title url:(nullable NSString *)url forExtensionContext:(WKWebExtensionContext *)context completionHandler:(void (^)(NSObject<_WKWebExtensionBookmark> *, NSError *))completionHandler;
```

## Discussion
`bookmarks.update` から呼び出される。未実装なら `it is not implemented` を返し、戻りの bookmark が `nil`/無効ならエラーに変換する。

## References
- [`WKWebExtensionControllerDelegatePrivate.h#L143`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerDelegatePrivate.h#L143)
- [`WebExtensionContextAPIBookmarksCocoa.mm#L540`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPIBookmarksCocoa.mm#L540)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
