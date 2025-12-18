# ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate/_webExtensionController(_:removeBookmarkWithIdentifier:removeFolderWithChildren:forExtensionContext:completionHandler:)``

ブックマーク/フォルダ削除を要求する。

## Objective-C Declaration
```objective-c
- (void)_webExtensionController:(WKWebExtensionController * _Nonnull)controller removeBookmarkWithIdentifier:(NSString *)bookmarkIdentifier removeFolderWithChildren:(BOOL)removeFolderWithChildren forExtensionContext:(WKWebExtensionContext * _Nonnull)context completionHandler:(void (^)(NSError * _Nullable))completionHandler;
```

## Discussion
`bookmarks.remove` は `removeFolderWithChildren=NO`、`bookmarks.removeTree` は `YES` で呼び出す。未実装なら `it is not implemented` を返し、エラーがあれば伝播する。

## References
- [`WKWebExtensionControllerDelegatePrivate.h#L153`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerDelegatePrivate.h#L153)
- [`WebExtensionContextAPIBookmarksCocoa.mm#L629`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPIBookmarksCocoa.mm#L629)
- [`WebExtensionContextAPIBookmarksCocoa.mm#L658`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPIBookmarksCocoa.mm#L658)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
