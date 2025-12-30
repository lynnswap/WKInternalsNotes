# ``WKInternalsNotes/_WKWebExtensionSidebar/iconForSize(_:)``

サイズ指定でサイドバーアイコンを返す。

## Objective-C Declaration
```objective-c
- (nullable UIImage *)iconForSize:(CGSize)size;
```

## Discussion
`WebExtensionSidebar::icon` を `CocoaImage` に変換して返す。`ENABLE(WK_WEB_EXTENSIONS_SIDEBAR)` が無効な場合は `nil` を返す。

## References
- [`_WKWebExtensionSidebar.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebar.h#L68)
- [`_WKWebExtensionSidebar.mm#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebar.mm#L59)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
