# ``WKInternalsNotes/WKPreferences/_safeBrowsingEnabled``

Safe Browsing を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, getter=_isSafeBrowsingEnabled, setter=_setSafeBrowsingEnabled:) BOOL _safeBrowsingEnabled WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Details
- Public API: `WKPreferences.fraudulentWebsiteWarningEnabled`
- WebPreferences key: `SafeBrowsingEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L155`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L155)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm)
- [`Source/WebKit/UIProcess/WebPageProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6578`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6578) (key: `SafeBrowsingEnabled`)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.h)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
