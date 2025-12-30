# ``WKInternalsNotes/_WKWebExtensionBookmark/urlStringForWebExtensionContext(_:)``

ブックマークの URL 文字列を返す。

## Objective-C Declaration
```objective-c
- (nullable NSString *)urlStringForWebExtensionContext:(WKWebExtensionContext * _Nonnull)context NS_SWIFT_NAME(url(for:));
```

## Discussion
ブックマークパラメータ生成で `url` を設定するために呼ばれる。

## References
- [`_WKWebExtensionBookmarks.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionBookmarks.h#L54)
- [`WebExtensionContextAPIBookmarksCocoa.mm#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPIBookmarksCocoa.mm#L44)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
