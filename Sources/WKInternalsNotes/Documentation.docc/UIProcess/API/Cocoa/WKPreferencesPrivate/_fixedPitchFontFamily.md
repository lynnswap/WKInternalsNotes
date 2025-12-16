# ``WKInternalsNotes/WKPreferencesPrivate/_fixedPitchFontFamily``

Fixed Font Family を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setFixedPitchFontFamily:) NSString *_fixedPitchFontFamily WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `"Courier New"_str` / macOS: `"Courier New"_str`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_fixedPitchFontFamily` を設定すると: Fixed Font Family を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: WebCore は fixed font family を `SettingsBase::setFixedFontFamily` / `SettingsBase::fixedFontFamily`（[`Source/WebCore/page/SettingsBase.cpp#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/SettingsBase.cpp#L121)）経由で保持/参照する。

## Details
- WebPreferences key: `FixedFontFamily`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L105`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L105)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L546`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L546)
- [`Source/WebCore/page/SettingsBase.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/SettingsBase.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2990`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2990) (key: `FixedFontFamily`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
