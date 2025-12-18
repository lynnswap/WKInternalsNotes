# ``WKInternalsNotes/WKWebViewConfiguration/_allowsMetaRefresh``

`<meta http-equiv=refresh>` を許可

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowsMetaRefresh:) BOOL _allowsMetaRefresh WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_allowsMetaRefresh = YES`: `<meta http-equiv=refresh>` を許可。
- `_allowsMetaRefresh = NO`: `<meta http-equiv=refresh>` を許可（無効）。

## References
- [`WKWebViewConfigurationPrivate.h#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L79)
- [`WKWebViewConfiguration.mm#L825`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L825)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
