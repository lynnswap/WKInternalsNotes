# ``WKInternalsNotes/_WKWebExtensionSidebar/webExtensionContext``

関連する `WKWebExtensionContext` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, readonly, weak) WKWebExtensionContext *webExtensionContext;
```

## Default Value
関連付けがない場合は `nil`。

## Discussion
`WebExtensionSidebar::extensionContext()` を wrapper 化して返す。`ENABLE(WK_WEB_EXTENSIONS_SIDEBAR)` が無効な場合は `nil` を返す。

## References
- [`_WKWebExtensionSidebar.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebar.h#L54)
- [`_WKWebExtensionSidebar.mm#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebar.mm#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
