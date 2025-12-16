# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_webExtensionController``

`_WKWebExtensionController`（実体は `WKWebExtensionController`）

## Objective-C Declaration
```objective-c
@property (nonatomic, strong, setter=_setWebExtensionController:) _WKWebExtensionController *_webExtensionController;
```

## Default Value
iOS: `nil` / macOS: `nil`

## Details
- Public API: `WKWebViewConfiguration.webExtensionController`（macOS 15.4 / iOS 18.4 / visionOS 2.4 以降）
- `ENABLE(WK_WEB_EXTENSIONS)` のみ

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L70)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L425`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L425)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
