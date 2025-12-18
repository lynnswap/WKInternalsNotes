# ``WKInternalsNotes/WKWebViewConfiguration/_systemPreviewEnabled``

system preview を有効化

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setSystemPreviewEnabled:) BOOL _systemPreviewEnabled WK_API_AVAILABLE(ios(12.0));
```

## Default Value
iOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_systemPreviewEnabled = YES`: system preview を有効化。
- `_systemPreviewEnabled = NO`: system preview を有効化（無効）。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L120)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L259`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L259)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
