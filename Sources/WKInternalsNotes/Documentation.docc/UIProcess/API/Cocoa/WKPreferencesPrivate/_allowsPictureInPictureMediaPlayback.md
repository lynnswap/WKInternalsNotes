# ``WKInternalsNotes/WKPreferences/_allowsPictureInPictureMediaPlayback``

Picture In Picture Media Playback を許可/禁止する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowsPictureInPictureMediaPlayback:) BOOL _allowsPictureInPictureMediaPlayback WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Default Value
iOS: `YES` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_allowsPictureInPictureMediaPlayback = YES`: Picture In Picture Media Playback を許可する。
- `_allowsPictureInPictureMediaPlayback = NO`: Picture In Picture Media Playback を禁止する。
- Implementation: [`MediaElementSession.cpp#L1119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/MediaElementSession.cpp#L1119) の `MediaElementSession::allowsPictureInPicture` が `allowsPictureInPictureMediaPlayback()` を参照する。

## Details
- WebPreferences key: `AllowsPictureInPictureMediaPlayback`
- Candidate Public API: `WKWebViewConfiguration.allowsPictureInPictureMediaPlayback` (iOS only)
- 備考: `WKWebView` 初期化時に `WKWebViewConfiguration.allowsPictureInPictureMediaPlayback` が内部の WebPreferences に反映される（ただし条件で抑制されることがある）。

## References
- [`WKPreferencesPrivate.h#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L109)
- [`WKPreferences.mm#L306`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L306)
- [`WKWebViewConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h)
- [`WKWebView.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm)
- [`MediaElementSession.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/MediaElementSession.cpp)
- [`UnifiedWebPreferences.yaml#L384`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L384) (key: `AllowsPictureInPictureMediaPlayback`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
