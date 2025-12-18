# ``WKInternalsNotes/WKPreferences/_mockCaptureDevicesEnabled``

Mock Capture Devices を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMockCaptureDevicesEnabled:) BOOL _mockCaptureDevicesEnabled WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_mockCaptureDevicesEnabled = YES`: Mock Capture Devices を有効化する。
- `_mockCaptureDevicesEnabled = NO`: Mock Capture Devices を無効化する。
- Implementation: [`SettingsBase.cpp#L434`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/SettingsBase.cpp#L434) の `SettingsBase::mockCaptureDevicesEnabledChanged` が `mockCaptureDevicesEnabled()` を参照する。

## Details
- WebPreferences key: `MockCaptureDevicesEnabled`

## References
- [`WKPreferencesPrivate.h#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L119)
- [`WKPreferences.mm#L690`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L690)
- [`SettingsBase.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/SettingsBase.cpp)
- [`UnifiedWebPreferences.yaml#L5317`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5317) (key: `MockCaptureDevicesEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
