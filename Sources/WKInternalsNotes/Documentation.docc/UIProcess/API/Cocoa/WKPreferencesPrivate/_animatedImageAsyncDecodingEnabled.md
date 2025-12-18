# ``WKInternalsNotes/WKPreferences/_animatedImageAsyncDecodingEnabled``

Animated Image Async Decoding を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAnimatedImageAsyncDecodingEnabled:) BOOL _animatedImageAsyncDecodingEnabled WK_API_AVAILABLE(macos(10.12.4), ios(10.3));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_animatedImageAsyncDecodingEnabled = YES`: Animated Image Async Decoding を有効化する。
- `_animatedImageAsyncDecodingEnabled = NO`: Animated Image Async Decoding を無効化する。
- Implementation: [`RenderBoxModelObject.cpp#L303`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/rendering/RenderBoxModelObject.cpp#L303) の `RenderBoxModelObject::decodingModeForImageDraw` が `animatedImageAsyncDecodingEnabled()` を参照する。

## Details
- WebPreferences key: `AnimatedImageAsyncDecodingEnabled`

## References
- [`WKPreferencesPrivate.h#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L85)
- [`WKPreferences.mm#L416`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L416)
- [`RenderBoxModelObject.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/rendering/RenderBoxModelObject.cpp)
- [`UnifiedWebPreferences.yaml#L457`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L457) (key: `AnimatedImageAsyncDecodingEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
