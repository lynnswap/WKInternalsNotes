# ``WKInternalsNotes/WKPreferencesPrivate/_mediaSourceEnabled``

Media Source API を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMediaSourceEnabled:) BOOL _mediaSourceEnabled WK_API_AVAILABLE(macos(10.13.4), ios(13.0));
```

## Default Value
条件付き: `ENABLE(MEDIA_SOURCE) && PLATFORM(IOS_FAMILY): WebKit::defaultMediaSourceEnabled() / ENABLE(MEDIA_SOURCE) && !PLATFORM(IOS_FAMILY): YES / default: NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_mediaSourceEnabled = YES`: Media Source API を有効化する。
- `_mediaSourceEnabled = NO`: Media Source API を無効化する。
- Implementation: [`Source/WebCore/Modules/mediasource/AudioTrack+MediaSource.idl#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediasource/AudioTrack+MediaSource.idl#L31)（`EnabledBySetting=MediaSourceEnabled`）

## Details
- WebPreferences key: `MediaSourceEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L165`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L165)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L918`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L918)
- [`Source/WebCore/Modules/mediasource/AudioTrack+MediaSource.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediasource/AudioTrack+MediaSource.idl)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5157`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5157) (key: `MediaSourceEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
