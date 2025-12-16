# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_needsStorageAccessFromFileURLsQuirk``

`file://` からの Storage Access の quirk

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setNeedsStorageAccessFromFileURLsQuirk:) BOOL _needsStorageAccessFromFileURLsQuirk WK_API_AVAILABLE(macos(10.12.4), ios(10.3));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_needsStorageAccessFromFileURLsQuirk = YES`: `file://` からの Storage Access の quirk。
- `_needsStorageAccessFromFileURLsQuirk = NO`: `file://` からの Storage Access の quirk（無効）。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L82)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1357`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1357)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
