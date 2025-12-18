# ``WKInternalsNotes/WKPreferences/_interruptAudioOnPageVisibilityChangeEnabled``

Interrupt Audio On Page Visibility Change を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setInterruptAudioOnPageVisibilityChangeEnabled:) BOOL _interruptAudioOnPageVisibilityChangeEnabled WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Default Value
iOS: `YES` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_interruptAudioOnPageVisibilityChangeEnabled = YES`: Interrupt Audio On Page Visibility Change を有効化する。
- `_interruptAudioOnPageVisibilityChangeEnabled = NO`: Interrupt Audio On Page Visibility Change を無効化する。
- Implementation: [`Document.cpp#L6129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp#L6129) の `Document::pageMutedStateDidChange` が `interruptAudioOnPageVisibilityChangeEnabled()` を参照する。

## Details
- WebPreferences key: `InterruptAudioOnPageVisibilityChangeEnabled`

## References
- [`WKPreferencesPrivate.h#L126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L126)
- [`WKPreferences.mm#L740`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L740)
- [`Document.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp)
- [`UnifiedWebPreferences.yaml#L4022`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4022) (key: `InterruptAudioOnPageVisibilityChangeEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
