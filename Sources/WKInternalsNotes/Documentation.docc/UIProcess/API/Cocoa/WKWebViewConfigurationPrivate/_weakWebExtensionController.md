# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_weakWebExtensionController``

弱参照の WebExtensionController

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setWeakWebExtensionController:) WKWebExtensionController *_weakWebExtensionController;
```

## Default Value
iOS: `nil` / macOS: `nil`

## Details
- Public API: `WKWebViewConfiguration.webExtensionController`（macOS 15.4 / iOS 18.4 / visionOS 2.4 以降。公開API は strong 参照）
- `ENABLE(WK_WEB_EXTENSIONS)` のみ

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L69)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L413`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L413)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
