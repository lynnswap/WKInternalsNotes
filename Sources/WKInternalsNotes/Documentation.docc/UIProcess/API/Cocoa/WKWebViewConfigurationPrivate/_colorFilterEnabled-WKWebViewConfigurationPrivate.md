# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_colorFilterEnabled``

color filter を有効化

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setColorFilterEnabled:) BOOL _colorFilterEnabled WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_colorFilterEnabled = YES`: color filter を有効化。
- `_colorFilterEnabled = NO`: color filter を有効化（無効）。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L94`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L94)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1050`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1050)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
