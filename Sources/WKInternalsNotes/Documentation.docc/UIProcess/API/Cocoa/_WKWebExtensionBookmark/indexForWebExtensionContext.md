# ``WKInternalsNotes/_WKWebExtensionBookmark/indexForWebExtensionContext(_:)``

親内の順序を返す。

## Objective-C Declaration
```objective-c
- (NSInteger)indexForWebExtensionContext:(WKWebExtensionContext * _Nonnull)context NS_SWIFT_NAME(index(for:));
```

## Discussion
ブックマークパラメータ生成で `index` を設定するために呼ばれる。

## References
- [`_WKWebExtensionBookmarks.h#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionBookmarks.h#L75)
- [`WebExtensionContextAPIBookmarksCocoa.mm#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPIBookmarksCocoa.mm#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
