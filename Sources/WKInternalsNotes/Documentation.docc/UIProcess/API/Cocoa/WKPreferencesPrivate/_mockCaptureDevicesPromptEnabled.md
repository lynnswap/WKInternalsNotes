# ``WKInternalsNotes/WKPreferencesPrivate/_mockCaptureDevicesPromptEnabled``

Mock Capture Devices Prompt を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMockCaptureDevicesPromptEnabled:) BOOL _mockCaptureDevicesPromptEnabled WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_mockCaptureDevicesPromptEnabled = YES`: Mock Capture Devices Prompt を有効化する。
- `_mockCaptureDevicesPromptEnabled = NO`: Mock Capture Devices Prompt を無効化する。
- Implementation: [`Source/WebKit/UIProcess/UserMediaPermissionRequestManagerProxy.cpp#L772`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/UserMediaPermissionRequestManagerProxy.cpp#L772) の `WebCore::RealtimeMediaSourceCenter::singleton` が `mockCaptureDevicesPromptEnabled()` を参照する。

## Details
- WebPreferences key: `MockCaptureDevicesPromptEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L120)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L700`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L700)
- [`Source/WebKit/UIProcess/UserMediaPermissionRequestManagerProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/UserMediaPermissionRequestManagerProxy.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5335`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5335) (key: `MockCaptureDevicesPromptEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
