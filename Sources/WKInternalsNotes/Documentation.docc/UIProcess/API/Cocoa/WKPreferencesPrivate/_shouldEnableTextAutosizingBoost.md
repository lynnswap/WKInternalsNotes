# ``WKInternalsNotes/WKPreferencesPrivate/_shouldEnableTextAutosizingBoost``

Text Autosizing Boost を切り替える API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setShouldEnableTextAutosizingBoost:) BOOL _shouldEnableTextAutosizingBoost WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_shouldEnableTextAutosizingBoost = YES`: Text Autosizing Boost を有効化する。
- `_shouldEnableTextAutosizingBoost = NO`: Text Autosizing Boost を無効化する。
- Implementation: [`Source/WebCore/page/SettingsBase.cpp#L410`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/SettingsBase.cpp#L410) の `SettingsBase::shouldEnableTextAutosizingBoostChanged` が `shouldEnableTextAutosizingBoost()` を参照する。

## Details
- WebPreferences key: `ShouldEnableTextAutosizingBoost`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L153`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L153)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1368`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1368)
- [`Source/WebCore/page/SettingsBase.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/SettingsBase.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7222`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7222) (key: `ShouldEnableTextAutosizingBoost`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
