# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_mediaCaptureEnabled``

media capture を有効化

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMediaCaptureEnabled:) BOOL _mediaCaptureEnabled WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_mediaCaptureEnabled = YES`: media capture を有効化。
- `_mediaCaptureEnabled = NO`: media capture を有効化（無効）。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L143`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L143)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1423`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1423)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
