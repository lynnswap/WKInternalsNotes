# ``WKInternalsNotes/WKWebViewConfiguration/_requiresUserActionForVideoPlayback``

video の再生に user action を要求

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setRequiresUserActionForVideoPlayback:) BOOL _requiresUserActionForVideoPlayback WK_API_DEPRECATED_WITH_REPLACEMENT("mediaTypesRequiringUserActionForPlayback", macos(10.12, 10.12), ios(10.0, 10.0));
```

## Default Value
iOS: `linkedOnOrAfterSDKWithBehavior(SDKAlignedBehavior::MediaTypesRequiringUserActionForPlayback) ? NO : YES` / macOS: `NO`

## Details
- Public API: `WKWebViewConfiguration.mediaTypesRequiringUserActionForPlayback`
- `mediaTypesRequiringUserActionForPlayback` 由来（SDK 依存）

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L136`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L136)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1173`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1173)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
