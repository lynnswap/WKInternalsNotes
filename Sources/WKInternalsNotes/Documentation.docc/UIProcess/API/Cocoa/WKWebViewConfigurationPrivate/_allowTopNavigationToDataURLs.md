# ``WKInternalsNotes/WKWebViewConfiguration/_allowTopNavigationToDataURLs``

top-level で `data:` への遷移を許可

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowTopNavigationToDataURLs:) BOOL _allowTopNavigationToDataURLs WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_allowTopNavigationToDataURLs = YES`: top-level で `data:` への遷移を許可。
- `_allowTopNavigationToDataURLs = NO`: top-level で `data:` への遷移を許可（無効）。

## References
- [`WKWebViewConfigurationPrivate.h#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L81)
- [`WKWebViewConfiguration.mm#L805`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L805)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
