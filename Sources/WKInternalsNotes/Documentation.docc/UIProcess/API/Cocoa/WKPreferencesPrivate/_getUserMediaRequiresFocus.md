# ``WKInternalsNotes/WKPreferences/_getUserMediaRequiresFocus``

Require focus to start getUserMedia を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setGetUserMediaRequiresFocus:) BOOL _getUserMediaRequiresFocus WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_getUserMediaRequiresFocus = YES`: Require focus to start getUserMedia を有効化する。
- `_getUserMediaRequiresFocus = NO`: Require focus to start getUserMedia を無効化する。
- Implementation: [`MediaDevices.cpp#L201`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediastream/MediaDevices.cpp#L201) の `UserMediaRequest::create` が `getUserMediaRequiresFocus()` を参照する。

## Details
- WebPreferences key: `GetUserMediaRequiresFocus`

## References
- [`WKPreferencesPrivate.h#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L117)
- [`WKPreferences.mm#L670`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L670)
- [`MediaDevices.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediastream/MediaDevices.cpp)
- [`UnifiedWebPreferences.yaml#L3281`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3281) (key: `GetUserMediaRequiresFocus`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
