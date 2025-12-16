# ``WKInternalsNotes/WKPreferencesPrivate/_videoFullscreenRequiresElementFullscreen``

Video Fullscreen Requires Element Fullscreen を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setVideoFullscreenRequiresElementFullscreen:) BOOL _videoFullscreenRequiresElementFullscreen WK_API_AVAILABLE(macos(15.2), ios(18.2), visionos(2.2));
```

## Default Value
iOS: `defaultVideoFullscreenRequiresElementFullscreen()` / macOS: `defaultVideoFullscreenRequiresElementFullscreen()` / visionOS: `defaultVideoFullscreenRequiresElementFullscreen()`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_videoFullscreenRequiresElementFullscreen = YES`: Video Fullscreen Requires Element Fullscreen を有効化する。
- `_videoFullscreenRequiresElementFullscreen = NO`: Video Fullscreen Requires Element Fullscreen を無効化する。
- Implementation: [`Source/WebCore/html/HTMLMediaElement.cpp#L7323`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLMediaElement.cpp#L7323) の `HTMLMediaElement::videoUsesElementFullscreen` が `videoFullscreenRequiresElementFullscreen()` を参照する。

## Details
- WebPreferences key: `VideoFullscreenRequiresElementFullscreen`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L197`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L197)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1660`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1660)
- [`Source/WebCore/html/HTMLMediaElement.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLMediaElement.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8593`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8593) (key: `VideoFullscreenRequiresElementFullscreen`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
