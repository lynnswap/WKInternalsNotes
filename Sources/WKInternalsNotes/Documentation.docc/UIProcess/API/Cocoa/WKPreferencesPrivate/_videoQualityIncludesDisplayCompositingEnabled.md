# ``WKInternalsNotes/WKPreferences/_videoQualityIncludesDisplayCompositingEnabled``

Video Quality Includes Display Compositing を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setVideoQualityIncludesDisplayCompositingEnabled:) BOOL _videoQualityIncludesDisplayCompositingEnabled WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_videoQualityIncludesDisplayCompositingEnabled = YES`: `VideoPlaybackQuality.displayCompositedVideoFrames` が利用可能になる。
- `_videoQualityIncludesDisplayCompositingEnabled = NO`: `VideoPlaybackQuality.displayCompositedVideoFrames` が利用できない。
- Implementation: [`VideoPlaybackQuality.idl#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediasource/VideoPlaybackQuality.idl#L41) が `EnabledBySetting=videoQualityIncludesDisplayCompositingEnabled` で `displayCompositedVideoFrames` を gated する。

## Details
- WebPreferences key: `VideoQualityIncludesDisplayCompositingEnabled`

## References
- [`WKPreferencesPrivate.h#L161`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L161)
- [`WKPreferences.mm#L1392`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1392)
- [`VideoPlaybackQuality.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediasource/VideoPlaybackQuality.idl)
- [`UnifiedWebPreferences.yaml#L8636`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8636) (key: `VideoQualityIncludesDisplayCompositingEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
