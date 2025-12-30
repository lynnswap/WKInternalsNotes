# ``WKInternalsNotes/_WKWebExtensionBookmark/titleForWebExtensionContext(_:)``

ブックマークのタイトルを返す。

## Objective-C Declaration
```objective-c
- (nullable NSString *)titleForWebExtensionContext:(WKWebExtensionContext * _Nonnull)context NS_SWIFT_NAME(title(for:));
```

## Discussion
ブックマークパラメータ生成で `title` を設定するために呼ばれる。

## References
- [`_WKWebExtensionBookmarks.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionBookmarks.h#L47)
- [`WebExtensionContextAPIBookmarksCocoa.mm#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPIBookmarksCocoa.mm#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
