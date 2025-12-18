# ``WKInternalsNotes/WKPreferences/_requiresUserGestureForVideoPlayback``

User Gesture For Video Playback を切り替える API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setRequiresUserGestureForVideoPlayback:) BOOL _requiresUserGestureForVideoPlayback WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_requiresUserGestureForVideoPlayback = YES`: User Gesture For Video Playback を有効化する。
- `_requiresUserGestureForVideoPlayback = NO`: User Gesture For Video Playback を無効化する。
- Implementation: [`Document.cpp#L7719`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp#L7719) の `Document::requiresUserGestureForVideoPlayback` が `requiresUserGestureForVideoPlayback()` を参照する。

## Details
- WebPreferences key: `RequiresUserGestureForVideoPlayback`
- Candidate Public API: `WKWebViewConfiguration.mediaTypesRequiringUserActionForPlayback`（Video bit で制御）

## References
- [`WKPreferencesPrivate.h#L233`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L233)
- [`WKPreferences.mm#L1269`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1269)
- [`WKWebViewConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h)
- [`WKWebView.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm)
- [`Document.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp)
- [`UnifiedWebPreferences.yaml#L6471`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6471) (key: `RequiresUserGestureForVideoPlayback`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
