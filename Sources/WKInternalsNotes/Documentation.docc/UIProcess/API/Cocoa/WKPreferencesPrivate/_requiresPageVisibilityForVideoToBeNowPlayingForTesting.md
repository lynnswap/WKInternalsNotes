# ``WKInternalsNotes/WKPreferences/_requiresPageVisibilityForVideoToBeNowPlayingForTesting``

Page Visibility For Video To Be Now Playing を切り替える API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setRequiresPageVisibilityForVideoToBeNowPlayingForTesting:) BOOL _requiresPageVisibilityForVideoToBeNowPlayingForTesting WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Default Value
iOS: `defaultRequiresPageVisibilityForVideoToBeNowPlaying()` / macOS: `defaultRequiresPageVisibilityForVideoToBeNowPlaying()` / visionOS: `defaultRequiresPageVisibilityForVideoToBeNowPlaying()`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_requiresPageVisibilityForVideoToBeNowPlayingForTesting = YES`: Page Visibility For Video To Be Now Playing を有効化する。
- `_requiresPageVisibilityForVideoToBeNowPlayingForTesting = NO`: Page Visibility For Video To Be Now Playing を無効化する。
- Implementation: [`HTMLMediaElement.cpp#L684`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLMediaElement.cpp#L684) の `MediaElementSession::create` が `requiresPageVisibilityForVideoToBeNowPlaying()` を参照する。

## Details
- WebPreferences key: `RequiresPageVisibilityForVideoToBeNowPlaying`

## References
- [`WKPreferencesPrivate.h#L203`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L203)
- [`WKPreferences.mm#L1730`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1730)
- [`HTMLMediaElement.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLMediaElement.cpp)
- [`UnifiedWebPreferences.yaml#L6422`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6422) (key: `RequiresPageVisibilityForVideoToBeNowPlaying`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
