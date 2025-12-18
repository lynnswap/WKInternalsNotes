# ``WKInternalsNotes/WKWebViewConfiguration/_strongWebExtensionController``

強参照の WebExtensionController

## Objective-C Declaration
```objective-c
@property (nonatomic, strong, readonly) WKWebExtensionController *_strongWebExtensionController;
```

## Default Value
iOS: `nil` / macOS: `nil`

## Details
- Public API: `WKWebViewConfiguration.webExtensionController`（macOS 15.4 / iOS 18.4 / visionOS 2.4 以降）
- `ENABLE(WK_WEB_EXTENSIONS)` のみ

## References
- [`WKWebViewConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h)
- [`WKWebViewConfigurationPrivate.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L68)
- [`WKWebViewConfiguration.mm#L404`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L404)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
