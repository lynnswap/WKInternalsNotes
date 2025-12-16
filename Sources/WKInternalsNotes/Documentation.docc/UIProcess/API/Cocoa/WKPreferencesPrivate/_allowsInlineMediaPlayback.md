# ``WKInternalsNotes/WKPreferencesPrivate/_allowsInlineMediaPlayback``

Inline Media Playback を許可/禁止する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowsInlineMediaPlayback:) BOOL _allowsInlineMediaPlayback WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_allowsInlineMediaPlayback = YES`: Inline Media Playback を許可する。
- `_allowsInlineMediaPlayback = NO`: Inline Media Playback を禁止する。
- Implementation: [`Source/WebCore/Modules/mediacontrols/MediaControlsHost.h#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediacontrols/MediaControlsHost.h#L90) で `allowsInlineMediaPlayback()` が参照される。

## Details
- WebPreferences key: `AllowsInlineMediaPlayback`
- Candidate Public API: `WKWebViewConfiguration.allowsInlineMediaPlayback` (iOS only)

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L224`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L224)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1179`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1179)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L796`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L796)
- [`Source/WebCore/Modules/mediacontrols/MediaControlsHost.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediacontrols/MediaControlsHost.h)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L356`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L356) (key: `AllowsInlineMediaPlayback`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
