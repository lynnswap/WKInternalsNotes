# ``WKInternalsNotes/_WKWebExtensionBookmark/childrenForWebExtensionContext(_:)``

子ブックマーク配列を返す。

## Objective-C Declaration
```objective-c
- (nullable NSArray<id<_WKWebExtensionBookmark>> *)childrenForWebExtensionContext:(WKWebExtensionContext * _Nonnull)context NS_SWIFT_NAME(children(for:));
```

## Discussion
ブックマークパラメータ生成やツリー探索で、子ノードがある場合に呼ばれる。

## References
- [`_WKWebExtensionBookmarks.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionBookmarks.h#L68)
- [`WebExtensionContextAPIBookmarksCocoa.mm#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPIBookmarksCocoa.mm#L46)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
