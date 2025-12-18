# ``WKInternalsNotes/WKPreferences/_loadsImagesAutomatically``

Loads Images Automatically を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setLoadsImagesAutomatically:) BOOL _loadsImagesAutomatically WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_loadsImagesAutomatically = YES`: Loads Images Automatically を有効化する。
- `_loadsImagesAutomatically = NO`: Loads Images Automatically を無効化する。
- Implementation: [`Source/WebCore/loader/FrameLoader.cpp#L823`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/loader/FrameLoader.cpp#L823) の `FrameLoader::didBeginDocument` が `loadsImagesAutomatically()` を参照する。

## Details
- WebPreferences key: `LoadsImagesAutomatically`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L113`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L113)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L640`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L640)
- [`Source/WebCore/loader/FrameLoader.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/loader/FrameLoader.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4567`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4567) (key: `LoadsImagesAutomatically`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
