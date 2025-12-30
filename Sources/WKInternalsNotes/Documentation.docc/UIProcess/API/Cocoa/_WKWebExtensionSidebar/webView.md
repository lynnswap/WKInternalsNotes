# ``WKInternalsNotes/_WKWebExtensionSidebar/webView``

サイドバー表示用の `WKWebView` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, readonly) WKWebView *webView;
```

## Default Value
タブ固有でない場合は `nil`。

## Discussion
`WebExtensionSidebar::webView()` を返す。`ENABLE(WK_WEB_EXTENSIONS_SIDEBAR)` が無効な場合は `nil` を返す。

## References
- [`_WKWebExtensionSidebar.h#L77`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebar.h#L77)
- [`_WKWebExtensionSidebar.mm#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebar.mm#L74)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
