# ``WKInternalsNotes/WKPreferencesPrivate/_requiresUserGestureForAudioPlayback``

User Gesture For Audio Playback を切り替える API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setRequiresUserGestureForAudioPlayback:) BOOL _requiresUserGestureForAudioPlayback WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_requiresUserGestureForAudioPlayback = YES`: User Gesture For Audio Playback を有効化する。
- `_requiresUserGestureForAudioPlayback = NO`: User Gesture For Audio Playback を無効化する。
- Implementation: [`Source/WebCore/Modules/speech/SpeechSynthesis.cpp#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/speech/SpeechSynthesis.cpp#L59) の `SpeechSynthesis::SpeechSynthesis` が `requiresUserGestureForAudioPlayback()` を参照する。

## Details
- WebPreferences key: `RequiresUserGestureForAudioPlayback`
- Candidate Public API: `WKWebViewConfiguration.mediaTypesRequiringUserActionForPlayback`（Audio bit で制御）

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L232`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L232)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1259`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1259)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm)
- [`Source/WebCore/Modules/speech/SpeechSynthesis.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/speech/SpeechSynthesis.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6445`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6445) (key: `RequiresUserGestureForAudioPlayback`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
