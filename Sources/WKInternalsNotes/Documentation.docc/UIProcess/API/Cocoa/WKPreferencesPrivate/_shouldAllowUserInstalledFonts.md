# ``WKInternalsNotes/WKPreferences/_shouldAllowUserInstalledFonts``

User Installed Fonts を切り替える API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setShouldAllowUserInstalledFonts:) BOOL _shouldAllowUserInstalledFonts WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_shouldAllowUserInstalledFonts = YES`: User Installed Fonts を有効化する。
- `_shouldAllowUserInstalledFonts = NO`: User Installed Fonts を無効化する。
- Implementation: [`FontCascadeCache.h#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/platform/graphics/FontCascadeCache.h#L125) の `FontDescriptionKeyRareData::create` が `shouldAllowUserInstalledFonts()` を参照する。

## Details
- WebPreferences key: `ShouldAllowUserInstalledFonts`

## References
- [`WKPreferencesPrivate.h#L131`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L131)
- [`WKPreferences.mm#L775`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L775)
- [`FontCascadeCache.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/platform/graphics/FontCascadeCache.h)
- [`UnifiedWebPreferences.yaml#L7114`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7114) (key: `ShouldAllowUserInstalledFonts`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
