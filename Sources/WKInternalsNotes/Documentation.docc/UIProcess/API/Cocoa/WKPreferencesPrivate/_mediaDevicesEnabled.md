# ``WKInternalsNotes/WKPreferences/_mediaDevicesEnabled``

media devices を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMediaDevicesEnabled:) BOOL _mediaDevicesEnabled WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_mediaDevicesEnabled = YES`: media devices を有効化する。
- `_mediaDevicesEnabled = NO`: media devices を無効化する。
- Implementation: [`Navigator+MediaDevices.idl#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediastream/Navigator+MediaDevices.idl#L35)（`EnabledBySetting=MediaDevicesEnabled`）

## Details
- WebPreferences key: `MediaDevicesEnabled`

## References
- [`WKPreferencesPrivate.h#L116`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L116)
- [`WKPreferences.mm#L660`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L660)
- [`Navigator+MediaDevices.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediastream/Navigator+MediaDevices.idl)
- [`UnifiedWebPreferences.yaml#L4988`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4988) (key: `MediaDevicesEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
