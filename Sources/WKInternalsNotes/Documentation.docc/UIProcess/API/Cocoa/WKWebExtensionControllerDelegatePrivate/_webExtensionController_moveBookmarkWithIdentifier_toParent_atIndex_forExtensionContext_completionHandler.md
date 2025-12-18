# ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate/_webExtensionController(_:moveBookmarkWithIdentifier:toParent:atIndex:forExtensionContext:completionHandler:)``

ブックマークの移動を要求する。

## Objective-C Declaration
```objective-c
- (void)_webExtensionController:(WKWebExtensionController *)controller moveBookmarkWithIdentifier:(NSString *)bookmarkId toParent:(nullable NSString *)parentId atIndex:(nullable NSNumber *)index forExtensionContext:(WKWebExtensionContext *)context completionHandler:(void (^)(NSObject<_WKWebExtensionBookmark> *, NSError *))completionHandler;
```

## Discussion
`bookmarks.move` から呼び出される。未実装なら `it is not implemented` を返し、戻りの bookmark が `nil`/無効ならエラーに変換する。

## References
- [`WKWebExtensionControllerDelegatePrivate.h#L175`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerDelegatePrivate.h#L175)
- [`WebExtensionContextAPIBookmarksCocoa.mm#L585`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPIBookmarksCocoa.mm#L585)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
