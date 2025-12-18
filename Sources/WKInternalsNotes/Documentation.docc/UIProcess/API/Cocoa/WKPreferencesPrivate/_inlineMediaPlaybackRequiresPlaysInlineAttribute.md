# ``WKInternalsNotes/WKPreferences/_inlineMediaPlaybackRequiresPlaysInlineAttribute``

Inline Media Playback Requires Plays Inline Attribute を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setInlineMediaPlaybackRequiresPlaysInlineAttribute:) BOOL _inlineMediaPlaybackRequiresPlaysInlineAttribute WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_inlineMediaPlaybackRequiresPlaysInlineAttribute = YES`: Inline Media Playback Requires Plays Inline Attribute を有効化する。
- `_inlineMediaPlaybackRequiresPlaysInlineAttribute = NO`: Inline Media Playback Requires Plays Inline Attribute を無効化する。
- Implementation: [`MediaElementSession.cpp#L1012`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/MediaElementSession.cpp#L1012) の `MediaElementSession::requiresFullscreenForVideoPlayback` が `inlineMediaPlaybackRequiresPlaysInlineAttribute()` を参照する。

## Details
- WebPreferences key: `InlineMediaPlaybackRequiresPlaysInlineAttribute`

## References
- [`WKPreferencesPrivate.h#L226`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L226)
- [`WKPreferences.mm#L1199`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1199)
- [`MediaElementSession.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/MediaElementSession.cpp)
- [`UnifiedWebPreferences.yaml#L3760`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3760) (key: `InlineMediaPlaybackRequiresPlaysInlineAttribute`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
