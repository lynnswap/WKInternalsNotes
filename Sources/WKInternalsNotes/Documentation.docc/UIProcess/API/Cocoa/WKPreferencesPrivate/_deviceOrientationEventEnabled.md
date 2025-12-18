# ``WKInternalsNotes/WKPreferences/_deviceOrientationEventEnabled``

Device Orientation Event を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setDeviceOrientationEventEnabled:) BOOL _deviceOrientationEventEnabled WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_deviceOrientationEventEnabled = YES`: Device Orientation Event を有効化する。
- `_deviceOrientationEventEnabled = NO`: Device Orientation Event を無効化する。
- Implementation: [`Source/WebKit/UIProcess/ios/WebDeviceOrientationUpdateProviderProxy.messages.in#L28`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDeviceOrientationUpdateProviderProxy.messages.in#L28)（`EnabledBy=DeviceOrientationEventEnabled`）

## Details
- WebPreferences key: `DeviceOrientationEventEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L162`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L162)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1404`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1404)
- [`Source/WebKit/UIProcess/ios/WebDeviceOrientationUpdateProviderProxy.messages.in`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebDeviceOrientationUpdateProviderProxy.messages.in)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2399`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2399) (key: `DeviceOrientationEventEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
