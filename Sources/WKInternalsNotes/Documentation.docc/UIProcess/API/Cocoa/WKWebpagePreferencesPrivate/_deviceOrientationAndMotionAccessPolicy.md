# ``WKInternalsNotes/WKWebpagePreferences/_deviceOrientationAndMotionAccessPolicy``

デバイス方向/モーションアクセスの許可ポリシーを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setDeviceOrientationAndMotionAccessPolicy:) _WKWebsiteDeviceOrientationAndMotionAccessPolicy _deviceOrientationAndMotionAccessPolicy;
```

## Default Value
`ENABLE(DEVICE_ORIENTATION)` 無効時は `_WKWebsiteDeviceOrientationAndMotionAccessPolicyDeny`。有効時は状態未設定なら `Ask` を返す。

## Discussion
setter は `ENABLE(DEVICE_ORIENTATION)` 有効時に `DeviceOrientationOrMotionPermissionState` へ変換して設定する。getter は `deviceOrientationAndMotionAccessState()` を逆変換し、未設定なら Ask を返す。

## References
- [`WKWebpagePreferencesPrivate.h#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L109)
- [`WKWebpagePreferences.mm#L336`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L336)
- [`WKWebpagePreferences.mm#L358`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L358)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
