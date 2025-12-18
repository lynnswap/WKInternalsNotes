# ``WKInternalsNotes/WKPreferences/_lowPowerVideoAudioBufferSizeEnabled``

Low Power Video Audio Buffer Size を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setLowPowerVideoAudioBufferSizeEnabled:) BOOL _lowPowerVideoAudioBufferSizeEnabled WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_lowPowerVideoAudioBufferSizeEnabled = YES`: Low Power Video Audio Buffer Size を有効化する。
- `_lowPowerVideoAudioBufferSizeEnabled = NO`: Low Power Video Audio Buffer Size を無効化する。
- Implementation: [`Source/WebCore/page/DeprecatedGlobalSettings.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/DeprecatedGlobalSettings.h#L53) で `lowPowerVideoAudioBufferSizeEnabled()` が参照される。

## Details
- WebPreferences key: `LowPowerVideoAudioBufferSizeEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L159`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L159)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L878`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L878)
- [`Source/WebCore/page/DeprecatedGlobalSettings.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/DeprecatedGlobalSettings.h#L53)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4694`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4694) (key: `LowPowerVideoAudioBufferSizeEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
