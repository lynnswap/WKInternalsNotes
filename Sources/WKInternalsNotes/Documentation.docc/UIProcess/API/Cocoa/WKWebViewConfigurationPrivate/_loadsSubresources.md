# ``WKInternalsNotes/WKWebViewConfiguration/_loadsSubresources``

subresource のロード可否

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setLoadsSubresources:) BOOL _loadsSubresources WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_loadsSubresources = YES`: subresource のロード可否。
- `_loadsSubresources = NO`: subresource のロード可否（無効）。

## References
- [`WKWebViewConfigurationPrivate.h#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L109)
- [`WKWebViewConfiguration.mm#L1148`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1148)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
