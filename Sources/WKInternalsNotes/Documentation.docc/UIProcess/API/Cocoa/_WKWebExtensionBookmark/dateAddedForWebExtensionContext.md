# ``WKInternalsNotes/_WKWebExtensionBookmark/dateAddedForWebExtensionContext(_:)``

追加日時を返す。

## Objective-C Declaration
```objective-c
- (nullable NSDate *)dateAddedForWebExtensionContext:(WKWebExtensionContext * _Nonnull)context NS_SWIFT_NAME(dateAdded(for:));
```

## Discussion
ブックマークパラメータ生成で `dateAdded` に変換して設定する。`nil` の場合は `0` 秒として扱われる。

## References
- [`_WKWebExtensionBookmarks.h#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionBookmarks.h#L82)
- [`WebExtensionContextAPIBookmarksCocoa.mm#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPIBookmarksCocoa.mm#L49)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
