# ``WKInternalsNotes/_WKWebExtensionSidebar/willOpenSidebar()``

サイドバーが開く直前に通知する。

## Objective-C Declaration
```objective-c
- (void)willOpenSidebar;
```

## Discussion
`WebExtensionSidebar::willOpenSidebar()` を呼ぶ。`ENABLE(WK_WEB_EXTENSIONS_SIDEBAR)` が無効な場合は no-op。

## References
- [`_WKWebExtensionSidebar.h#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebar.h#L101)
- [`_WKWebExtensionSidebar.mm#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebar.mm#L79)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
