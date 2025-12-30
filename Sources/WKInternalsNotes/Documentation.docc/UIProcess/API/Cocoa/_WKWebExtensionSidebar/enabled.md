# ``WKInternalsNotes/_WKWebExtensionSidebar/enabled``

サイドバーが有効かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isEnabled) BOOL enabled;
```

## Default Value
`ENABLE(WK_WEB_EXTENSIONS_SIDEBAR)` が無効な場合は `false`。

## Discussion
`WebExtensionSidebar::isEnabled()` を返す。

## References
- [`_WKWebExtensionSidebar.h#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebar.h#L73)
- [`_WKWebExtensionSidebar.mm#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebar.mm#L69)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
