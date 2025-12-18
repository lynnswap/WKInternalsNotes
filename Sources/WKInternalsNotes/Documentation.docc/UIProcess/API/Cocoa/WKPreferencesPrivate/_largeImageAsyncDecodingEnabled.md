# ``WKInternalsNotes/WKPreferences/_largeImageAsyncDecodingEnabled``

Large Image Async Decoding を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setLargeImageAsyncDecodingEnabled:) BOOL _largeImageAsyncDecodingEnabled WK_API_AVAILABLE(macos(10.12.4), ios(10.3));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_largeImageAsyncDecodingEnabled = YES`: Large Image Async Decoding を有効化する。
- `_largeImageAsyncDecodingEnabled = NO`: Large Image Async Decoding を無効化する。
- Implementation: [`Source/WebCore/rendering/RenderBoxModelObject.cpp#L303`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/rendering/RenderBoxModelObject.cpp#L303) の `RenderBoxModelObject::decodingModeForImageDraw` が `largeImageAsyncDecodingEnabled()` を参照する。

## Details
- WebPreferences key: `LargeImageAsyncDecodingEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L83)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L396`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L396)
- [`Source/WebCore/rendering/RenderBoxModelObject.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/rendering/RenderBoxModelObject.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4260`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4260) (key: `LargeImageAsyncDecodingEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
