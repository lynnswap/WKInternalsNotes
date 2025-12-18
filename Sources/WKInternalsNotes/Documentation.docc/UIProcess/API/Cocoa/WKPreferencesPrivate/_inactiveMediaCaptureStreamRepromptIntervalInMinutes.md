# ``WKInternalsNotes/WKPreferences/_inactiveMediaCaptureStreamRepromptIntervalInMinutes``

Inactive Media Capture Stream Reprompt Interval In Minutes を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setInactiveMediaCaptureStreamRepromptIntervalInMinutes:) double _inactiveMediaCaptureStreamRepromptIntervalInMinutes WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Default Value
iOS: `10` / macOS: `10`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_inactiveMediaCaptureStreamRepromptIntervalInMinutes` を設定すると: Inactive Media Capture Stream Reprompt Interval In Minutes を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: [`UserMediaPermissionRequestManagerProxy.cpp#L1173`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/UserMediaPermissionRequestManagerProxy.cpp#L1173) の `UserMediaPermissionRequestManagerProxy::captureStateChanged` が `inactiveMediaCaptureStreamRepromptIntervalInMinutes()` を watchdog interval 計算に使う。

## Details
- WebPreferences key: `InactiveMediaCaptureStreamRepromptIntervalInMinutes`

## References
- [`WKPreferencesPrivate.h#L124`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L124)
- [`WKPreferences.mm#L720`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L720)
- [`UserMediaPermissionRequestManagerProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/UserMediaPermissionRequestManagerProxy.cpp)
- [`UnifiedWebPreferences.yaml#L3671`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3671) (key: `InactiveMediaCaptureStreamRepromptIntervalInMinutes`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
