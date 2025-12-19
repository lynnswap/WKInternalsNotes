# ``WKInternalsNotes/WKWebExtension/_hasSidebar``

拡張にサイドバーがあるかどうかを示す。

## Objective-C Declaration
```objective-c
@property (readonly, nonatomic) BOOL _hasSidebar;
```

## Default Value
`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `NO`。`ENABLE(WK_WEB_EXTENSIONS_SIDEBAR)` が無効なビルドでも `NO`。有効時は `hasAnySidebar()` の結果に依存する。

## Discussion
`ENABLE(WK_WEB_EXTENSIONS_SIDEBAR)` の場合は `_webExtension->hasAnySidebar()` を返し、無効時は `NO`。`ENABLE(WK_WEB_EXTENSIONS)` 無効時も `NO`。

## References
- [`WKWebExtensionPrivate.h#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionPrivate.h#L100)
- [`WKWebExtension.mm#L331`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L331)
- [`WKWebExtension.mm#L331`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L331)
- [`WKWebExtension.mm#L331`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L331)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
