# ``WKInternalsNotes/_WKWebExtensionBookmark/parentIdentifierForWebExtensionContext(_:)``

親ブックマークの識別子を返す。

## Objective-C Declaration
```objective-c
- (nullable NSString *)parentIdentifierForWebExtensionContext:(WKWebExtensionContext * _Nonnull)context NS_SWIFT_NAME(parentIdentifier(for:));
```

## Discussion
ブックマークパラメータ生成で `parentId` を設定するために呼ばれる。

## References
- [`_WKWebExtensionBookmarks.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionBookmarks.h#L40)
- [`WebExtensionContextAPIBookmarksCocoa.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPIBookmarksCocoa.mm#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
