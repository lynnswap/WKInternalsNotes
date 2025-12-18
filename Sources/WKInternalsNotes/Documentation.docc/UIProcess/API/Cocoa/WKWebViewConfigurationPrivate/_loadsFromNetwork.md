# ``WKInternalsNotes/WKWebViewConfiguration/_loadsFromNetwork``

ネットワークからのロード可否

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setLoadsFromNetwork:) BOOL _loadsFromNetwork WK_API_DEPRECATED_WITH_REPLACEMENT("_allowedNetworkHosts", macos(11.0, 12.0), ios(14.0, 15.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_loadsFromNetwork = YES`: ネットワークからのロード可否。
- `_loadsFromNetwork = NO`: ネットワークからのロード可否（無効）。

## Details
- Deprecated（`_allowedNetworkHosts`）

## References
- [`WKWebViewConfigurationPrivate.h#L107`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L107)
- [`WKWebViewConfiguration.mm#L1117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1117)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
