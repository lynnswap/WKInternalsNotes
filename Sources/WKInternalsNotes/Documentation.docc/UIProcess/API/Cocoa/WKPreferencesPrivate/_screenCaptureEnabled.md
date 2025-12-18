# ``WKInternalsNotes/WKPreferences/_screenCaptureEnabled``

ScreenCapture を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setScreenCaptureEnabled:) BOOL _screenCaptureEnabled WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Default Value
条件付き: `PLATFORM(MAC) || USE(GSTREAMER): YES / default: NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_screenCaptureEnabled = YES`: ScreenCapture を有効化する。
- `_screenCaptureEnabled = NO`: ScreenCapture を無効化する。
- Implementation: [`MediaDevices.idl#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediastream/MediaDevices.idl#L44)（`EnabledBySetting=ScreenCaptureEnabled`）

## Details
- WebPreferences key: `ScreenCaptureEnabled`

## References
- [`WKPreferencesPrivate.h#L118`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L118)
- [`WKPreferences.mm#L680`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L680)
- [`MediaDevices.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediastream/MediaDevices.idl)
- [`UnifiedWebPreferences.yaml#L6643`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6643) (key: `ScreenCaptureEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
