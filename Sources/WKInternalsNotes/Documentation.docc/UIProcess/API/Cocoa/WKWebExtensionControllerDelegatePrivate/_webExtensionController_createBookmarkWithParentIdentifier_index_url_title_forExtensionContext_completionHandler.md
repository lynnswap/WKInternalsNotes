# ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate/_webExtensionController(_:createBookmarkWithParentIdentifier:index:url:title:forExtensionContext:completionHandler:)``

ブックマーク/フォルダ作成を要求する。

## Objective-C Declaration
```objective-c
- (void)_webExtensionController:(WKWebExtensionController * _Nonnull)controller createBookmarkWithParentIdentifier:(nullable NSString *)parentId index:(nullable NSNumber *)index url:(nullable NSString *)url title:(NSString * _Nonnull)title forExtensionContext:(WKWebExtensionContext * _Nonnull)context completionHandler:(void (^)(NSObject<_WKWebExtensionBookmark> * _Nullable, NSError * _Nullable))completionHandler;
```

## Discussion
`bookmarks.create` から呼び出される。未実装なら `it is not implemented` を返し、戻りの bookmark が `nil`/無効ならエラーに変換する。

## References
- [`WKWebExtensionControllerDelegatePrivate.h#L127`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerDelegatePrivate.h#L127)
- [`WebExtensionContextAPIBookmarksCocoa.mm#L170`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPIBookmarksCocoa.mm#L170)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
