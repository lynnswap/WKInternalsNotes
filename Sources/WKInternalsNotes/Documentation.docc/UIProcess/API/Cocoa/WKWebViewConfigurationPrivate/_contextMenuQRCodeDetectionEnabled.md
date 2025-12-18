# ``WKInternalsNotes/WKWebViewConfiguration/_contextMenuQRCodeDetectionEnabled``

コンテキストメニューの QR 検出

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setContextMenuQRCodeDetectionEnabled:) BOOL _contextMenuQRCodeDetectionEnabled WK_API_AVAILABLE(macos(14.0));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_contextMenuQRCodeDetectionEnabled = YES`: コンテキストメニューの QR 検出。
- `_contextMenuQRCodeDetectionEnabled = NO`: コンテキストメニューの QR 検出（無効）。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L129)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1280`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1280)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
