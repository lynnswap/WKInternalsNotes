# ``WKInternalsNotes/WKPreferences/_fullScreenEnabled``

Fullscreen API を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setFullScreenEnabled:) BOOL _fullScreenEnabled WK_API_DEPRECATED_WITH_REPLACEMENT("elementFullscreenEnabled", macos(10.11, 12.3), ios(9.0, 15.4));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Details
- Public API: `WKPreferences.elementFullscreenEnabled`
- WebPreferences key: `FullScreenEnabled`

## References
- [`WKPreferencesPrivate.h#L107`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L107)
- [`WKPreferences.mm#L296`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L296)
- [`Document+Fullscreen.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document+Fullscreen.idl)
- [`UnifiedWebPreferences.yaml#L3091`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3091) (key: `FullScreenEnabled`)
- [`WKPreferences.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.h)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
