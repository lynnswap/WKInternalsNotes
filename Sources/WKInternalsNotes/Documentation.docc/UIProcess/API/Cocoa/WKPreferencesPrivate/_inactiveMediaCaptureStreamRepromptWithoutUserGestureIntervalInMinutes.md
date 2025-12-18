# ``WKInternalsNotes/WKPreferences/_inactiveMediaCaptureStreamRepromptWithoutUserGestureIntervalInMinutes``

Inactive Media Capture Stream Reprompt Without User Gesture Interval In Minutes を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setInactiveMediaCaptureStreamRepromptWithoutUserGestureIntervalInMinutes:) double _inactiveMediaCaptureStreamRepromptWithoutUserGestureIntervalInMinutes WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA));
```

## Default Value
iOS: `defaultInactiveMediaCaptureStreamRepromptWithoutUserGestureIntervalInMinutes()` / macOS: `defaultInactiveMediaCaptureStreamRepromptWithoutUserGestureIntervalInMinutes()`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_inactiveMediaCaptureStreamRepromptWithoutUserGestureIntervalInMinutes` を設定すると: Inactive Media Capture Stream Reprompt Without User Gesture Interval In Minutes を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: [`Source/WebKit/UIProcess/UserMediaPermissionRequestManagerProxy.cpp#L446`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/UserMediaPermissionRequestManagerProxy.cpp#L446) の `UserMediaPermissionRequestManagerProxy::hasGrantedRequest` が `inactiveMediaCaptureStreamRepromptWithoutUserGestureIntervalInMinutes()` を参照する。

## Details
- WebPreferences key: `InactiveMediaCaptureStreamRepromptWithoutUserGestureIntervalInMinutes`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L125)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L730`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L730)
- [`Source/WebKit/UIProcess/UserMediaPermissionRequestManagerProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/UserMediaPermissionRequestManagerProxy.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3681`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3681) (key: `InactiveMediaCaptureStreamRepromptWithoutUserGestureIntervalInMinutes`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
