# ``WKInternalsNotes/WKWebViewConfiguration/_printsBackgrounds``

印刷時に背景を出力する

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setPrintsBackgrounds:) BOOL _printsBackgrounds WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `WebKit::defaultShouldPrintBackgrounds()` / macOS: `NO`

## Details
- Public API: `WKPreferences.shouldPrintBackgrounds`（macOS 13.3 / iOS 16.4 以降）
- iOS は SDK 依存（`linkedOnOrAfterSDKWithBehavior`）

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.h)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L75)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L735`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L735)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L767`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L767)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
