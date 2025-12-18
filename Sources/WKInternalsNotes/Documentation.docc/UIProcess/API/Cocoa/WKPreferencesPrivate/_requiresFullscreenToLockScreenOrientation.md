# ``WKInternalsNotes/WKPreferences/_requiresFullscreenToLockScreenOrientation``

Require being in Fullscreen to lock screen orientation を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setRequiresFullscreenToLockScreenOrientation:) BOOL _requiresFullscreenToLockScreenOrientation WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_requiresFullscreenToLockScreenOrientation = YES`: Require being in Fullscreen to lock screen orientation を有効化する。
- `_requiresFullscreenToLockScreenOrientation = NO`: Require being in Fullscreen to lock screen orientation を無効化する。
- Implementation: [`Source/WebCore/page/ScreenOrientation.cpp#L98`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/ScreenOrientation.cpp#L98) の `ScreenOrientation::lock` が `fullscreenRequirementForScreenOrientationLockingEnabled()` を参照する。

## Details
- WebPreferences key: `FullscreenRequirementForScreenOrientationLockingEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L188`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L188)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1580`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1580)
- [`Source/WebCore/page/ScreenOrientation.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/ScreenOrientation.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3124`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3124) (key: `FullscreenRequirementForScreenOrientationLockingEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
