# ``WKInternalsNotes/WKPreferencesPrivate/_mediaSessionEnabled``

Media Session API を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMediaSessionEnabled:) BOOL _mediaSessionEnabled WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_mediaSessionEnabled = YES`: Media Session API を有効化する。
- `_mediaSessionEnabled = NO`: Media Session API を無効化する。
- Implementation: [`Source/WebCore/Modules/mediasession/Navigator+MediaSession.idl#L29`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediasession/Navigator+MediaSession.idl#L29)（`EnabledBySetting=MediaSessionEnabled`）

## Details
- WebPreferences key: `MediaSessionEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L176`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L176)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1469`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1469)
- [`Source/WebCore/Modules/mediasession/Navigator+MediaSession.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediasession/Navigator+MediaSession.idl)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5127`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5127) (key: `MediaSessionEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
