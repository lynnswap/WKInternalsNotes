# ``WKInternalsNotes/WKWebViewConfiguration/_markedTextInputEnabled``

“marked text input” API（実装は `allowsInlinePredictions`）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMarkedTextInputEnabled:) BOOL _markedTextInputEnabled WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Details
- Public API: `WKWebViewConfiguration.allowsInlinePredictions`
- `WKWebViewConfiguration.mm` 内に “FIXME: Remove this API …” あり

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L172`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L172)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1561`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1561)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
