# ``WKInternalsNotes/_WKWebExtensionSidebar/title``

サイドバーのタイトルを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *title;
```

## Default Value
固定値はなく、内部状態から取得される。

## Discussion
`WebExtensionSidebar::title()` を返す。`ENABLE(WK_WEB_EXTENSIONS_SIDEBAR)` が無効な場合は `nil` を返す。

## References
- [`_WKWebExtensionSidebar.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebar.h#L59)
- [`_WKWebExtensionSidebar.mm#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebar.mm#L54)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
