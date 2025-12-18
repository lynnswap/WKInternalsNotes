# ``WKInternalsNotes/WKPreferences/_mediaCapabilityGrantsEnabled``

Media Capability Grants を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMediaCapabilityGrantsEnabled:) BOOL _mediaCapabilityGrantsEnabled WK_API_AVAILABLE(ios(17.4), visionos(1.1)) WK_API_UNAVAILABLE(macos);
```

## Default Value
iOS: `YES` / visionOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_mediaCapabilityGrantsEnabled = YES`: Media Capability Grants を有効化する。
- `_mediaCapabilityGrantsEnabled = NO`: Media Capability Grants を無効化する。
- Implementation: [`Source/WebKit/UIProcess/Cocoa/WebPageProxyCocoa.mm#L1197`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WebPageProxyCocoa.mm#L1197) の `WebPageProxy::resetMediaCapability` が `mediaCapabilityGrantsEnabled()` を参照する。

## Details
- WebPreferences key: `MediaCapabilityGrantsEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L195)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1635`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1635)
- [`Source/WebKit/UIProcess/Cocoa/WebPageProxyCocoa.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WebPageProxyCocoa.mm)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4858`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4858) (key: `MediaCapabilityGrantsEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
