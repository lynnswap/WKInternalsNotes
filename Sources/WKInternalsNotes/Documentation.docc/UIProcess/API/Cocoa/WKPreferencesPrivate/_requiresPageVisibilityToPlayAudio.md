# ``WKInternalsNotes/WKPreferences/_requiresPageVisibilityToPlayAudio``

Page Visibility To Play Audio を切り替える API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setRequiresPageVisibilityToPlayAudio:) BOOL _requiresPageVisibilityToPlayAudio WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_requiresPageVisibilityToPlayAudio = YES`: Page Visibility To Play Audio を有効化する。
- `_requiresPageVisibilityToPlayAudio = NO`: Page Visibility To Play Audio を無効化する。
- Implementation: [`Source/WebCore/html/HTMLMediaElement.cpp#L684`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLMediaElement.cpp#L684) の `MediaElementSession::create` が `requiresPageVisibilityToPlayAudio()` を参照する。

## Details
- WebPreferences key: `RequiresPageVisibilityToPlayAudio`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L178`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L178)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1495`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1495)
- [`Source/WebCore/html/HTMLMediaElement.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLMediaElement.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6434`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6434) (key: `RequiresPageVisibilityToPlayAudio`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
