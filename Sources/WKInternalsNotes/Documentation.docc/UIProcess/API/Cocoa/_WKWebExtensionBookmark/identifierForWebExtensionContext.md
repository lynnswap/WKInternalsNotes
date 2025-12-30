# ``WKInternalsNotes/_WKWebExtensionBookmark/identifierForWebExtensionContext(_:)``

ブックマークの識別子を返す。

## Objective-C Declaration
```objective-c
- (NSString *)identifierForWebExtensionContext:(WKWebExtensionContext * _Nonnull)context NS_SWIFT_NAME(identifier(for:));
```

## Discussion
ブックマークパラメータ生成で `nodeId` を設定するために呼ばれる。`nil` を返すと変換が失敗する。

## References
- [`_WKWebExtensionBookmarks.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionBookmarks.h#L33)
- [`WebExtensionContextAPIBookmarksCocoa.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPIBookmarksCocoa.mm#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
