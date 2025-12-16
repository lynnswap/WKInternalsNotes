# ``WKInternalsNotes/WKPreferencesPrivate/_needsSiteSpecificQuirks``

site-specific quirks を切り替える API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setNeedsSiteSpecificQuirks:) BOOL _needsSiteSpecificQuirks WK_API_DEPRECATED_WITH_REPLACEMENT("siteSpecificQuirksModeEnabled", macos(10.13.4, 13.0), ios(13.0, 16.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Details
- Public API: `WKPreferences.siteSpecificQuirksModeEnabled`
- WebPreferences key: `NeedsSiteSpecificQuirks`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L163`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L163)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L898`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L898)
- [`Source/WebCore/bindings/js/JSDOMWindowBase.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/bindings/js/JSDOMWindowBase.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5575`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5575) (key: `NeedsSiteSpecificQuirks`)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.h)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
