# ``WKInternalsNotes/WKWebViewConfiguration/_attachmentElementEnabled``

attachment element を有効化

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAttachmentElementEnabled:) BOOL _attachmentElementEnabled WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_attachmentElementEnabled = YES`: attachment element を有効化。
- `_attachmentElementEnabled = NO`: attachment element を有効化（無効）。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L86)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1017`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1017)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
