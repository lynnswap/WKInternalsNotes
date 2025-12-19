# ``WKInternalsNotes/WKWebExtensionContext/sidebarForTab(_:)``

指定タブのサイドバー（またはデフォルト）を返す。

## Objective-C Declaration
```objective-c
- (nullable _WKWebExtensionSidebar *)sidebarForTab:(nullable id <WKWebExtensionTab>)tab NS_SWIFT_NAME(sidebar(for:));
```

## Discussion
`ENABLE(WK_WEB_EXTENSIONS_SIDEBAR)` の場合は `getOrCreateSidebar(...)` を呼び、取得できたら wrapper を返す。無効時は `nil`。`ENABLE(WK_WEB_EXTENSIONS)` 無効時も `nil`。

## References
- [`WKWebExtensionContextPrivate.h#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContextPrivate.h#L71)
- [`WKWebExtensionContext.mm#L873`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L873)
- [`WKWebExtensionContext.mm#L873`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L873)
- [`WKWebExtensionContext.mm#L873`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L873)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
