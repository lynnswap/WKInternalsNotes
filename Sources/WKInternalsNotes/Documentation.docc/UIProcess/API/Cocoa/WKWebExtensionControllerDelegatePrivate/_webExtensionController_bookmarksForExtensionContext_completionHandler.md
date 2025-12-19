# ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate/_webExtensionController(_:bookmarksForExtensionContext:completionHandler:)``

ブックマークツリー取得のためにトップレベルを要求する。

## Objective-C Declaration
```objective-c
- (void)_webExtensionController:(WKWebExtensionController * _Nonnull)controller bookmarksForExtensionContext:(WKWebExtensionContext * _Nonnull)context completionHandler:(void (^)(NSArray<NSObject<_WKWebExtensionBookmark> *> * _Nullable, NSError * _Nullable))completionHandler;
```

## Discussion
`bookmarks.getTree` などで delegate 実装を要求し、未実装なら `it is not implemented` のエラーを返す。返却配列が `nil` の場合もエラー扱い。

## References
- [`WKWebExtensionControllerDelegatePrivate.h#L107`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerDelegatePrivate.h#L107)
- [`WebExtensionContextAPIBookmarksCocoa.mm#L209`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPIBookmarksCocoa.mm#L209)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
