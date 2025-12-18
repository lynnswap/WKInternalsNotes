# ``WKInternalsNotes/WKPreferences/_remotePlaybackEnabled``

Remote Playback API を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setRemotePlaybackEnabled:) BOOL _remotePlaybackEnabled WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_remotePlaybackEnabled = YES`: Remote Playback API を有効化する。
- `_remotePlaybackEnabled = NO`: Remote Playback API を無効化する。
- Implementation: [`Source/WebCore/Modules/remoteplayback/HTMLMediaElement+RemotePlayback.idl#L30`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/remoteplayback/HTMLMediaElement+RemotePlayback.idl#L30)（`EnabledBySetting=RemotePlaybackEnabled`）

## Details
- WebPreferences key: `RemotePlaybackEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L167`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L167)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L983`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L983)
- [`Source/WebCore/Modules/remoteplayback/HTMLMediaElement+RemotePlayback.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/remoteplayback/HTMLMediaElement+RemotePlayback.idl)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6304`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6304) (key: `RemotePlaybackEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
