# ``WKInternalsNotes/_WKWebExtensionBookmark/bookmarkTypeForWebExtensionContext(_:)``

ブックマーク種別を返す。

## Objective-C Declaration
```objective-c
- (_WKWebExtensionBookmarkType)bookmarkTypeForWebExtensionContext:(WKWebExtensionContext * _Nonnull)context NS_SWIFT_NAME(bookmarkType(for:));
```

## Discussion
ブックマークのフラット化処理やフォルダ判定で参照される。

## References
- [`_WKWebExtensionBookmarks.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionBookmarks.h#L61)
- [`WebExtensionContextAPIBookmarksCocoa.mm#L128`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPIBookmarksCocoa.mm#L128)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
