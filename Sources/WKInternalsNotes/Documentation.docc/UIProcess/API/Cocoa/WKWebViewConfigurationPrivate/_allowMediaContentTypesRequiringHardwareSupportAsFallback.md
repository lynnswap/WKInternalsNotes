# ``WKInternalsNotes/WKWebViewConfiguration/_allowMediaContentTypesRequiringHardwareSupportAsFallback``

HW 必須 type を fallback として許可

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowMediaContentTypesRequiringHardwareSupportAsFallback:) BOOL _allowMediaContentTypesRequiringHardwareSupportAsFallback WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_allowMediaContentTypesRequiringHardwareSupportAsFallback = YES`: HW 必須 type を fallback として許可。
- `_allowMediaContentTypesRequiringHardwareSupportAsFallback = NO`: HW 必須 type を fallback として許可（無効）。

## References
- [`WKWebViewConfigurationPrivate.h#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L141)
- [`WKWebViewConfiguration.mm#L1418`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1418)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
