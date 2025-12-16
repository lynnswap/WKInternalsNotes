# ``WKInternalsNotes/WKPreferencesPrivate/_shouldPrintBackgrounds``

Print Backgrounds を切り替える API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setShouldPrintBackgrounds:) BOOL _shouldPrintBackgrounds WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `NO`

## Details
- Public API: `WKPreferences.shouldPrintBackgrounds`
- WebPreferences key: `ShouldPrintBackgrounds`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L215`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L215)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1079`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1079)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7247`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7247) (key: `ShouldPrintBackgrounds`)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.h)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
