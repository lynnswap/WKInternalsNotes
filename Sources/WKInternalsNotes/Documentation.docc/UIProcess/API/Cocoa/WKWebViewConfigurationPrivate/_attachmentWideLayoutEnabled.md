# ``WKInternalsNotes/WKWebViewConfiguration/_attachmentWideLayoutEnabled``

attachment の wide layout を有効化

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAttachmentWideLayoutEnabled:) BOOL _attachmentWideLayoutEnabled WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_attachmentWideLayoutEnabled = YES`: attachment の wide layout を有効化。
- `_attachmentWideLayoutEnabled = NO`: attachment の wide layout を有効化（無効）。

## References
- [`WKWebViewConfigurationPrivate.h#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L87)
- [`WKWebViewConfiguration.mm#L1027`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1027)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
