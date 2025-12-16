# ``WKInternalsNotes/WKPreferencesPrivate/_peerConnectionEnabled``

RTCPeerConnection を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setPeerConnectionEnabled:) BOOL _peerConnectionEnabled WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_peerConnectionEnabled = YES`: RTCPeerConnection を有効化する。
- `_peerConnectionEnabled = NO`: RTCPeerConnection を無効化する。
- Implementation: [`Source/WebCore/Modules/mediastream/RTCAnswerOptions.idl#L28`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediastream/RTCAnswerOptions.idl#L28)（`EnabledBySetting=PeerConnectionEnabled`）

## Details
- WebPreferences key: `PeerConnectionEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L115`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L115)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L650`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L650)
- [`Source/WebCore/Modules/mediastream/RTCAnswerOptions.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediastream/RTCAnswerOptions.idl)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5914`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5914) (key: `PeerConnectionEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
