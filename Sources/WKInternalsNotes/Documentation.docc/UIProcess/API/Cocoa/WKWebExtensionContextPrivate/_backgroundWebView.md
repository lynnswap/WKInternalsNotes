# ``WKInternalsNotes/WKWebExtensionContext/_backgroundWebView``

拡張のバックグラウンド用 WebView を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, readonly) WKWebView *_backgroundWebView;
```

## Default Value
`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `nil`。有効時は `backgroundWebView()` の結果（バックグラウンドコンテンツがない/未ロードなら `nil`）。

## Discussion
`_protectedWebExtensionContext->backgroundWebView()` を返す。`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `nil`。

## References
- [`WKWebExtensionContextPrivate.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContextPrivate.h#L35)
- [`WKWebExtensionContext.mm#L845`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L845)
- [`WKWebExtensionContext.mm#L845`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L845)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
