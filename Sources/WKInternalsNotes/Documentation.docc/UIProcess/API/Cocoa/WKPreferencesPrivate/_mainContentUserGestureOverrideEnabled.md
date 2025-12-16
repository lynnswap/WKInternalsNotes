# ``WKInternalsNotes/WKPreferencesPrivate/_mainContentUserGestureOverrideEnabled``

main content user gesture override を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMainContentUserGestureOverrideEnabled:) BOOL _mainContentUserGestureOverrideEnabled WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_mainContentUserGestureOverrideEnabled = YES`: main content user gesture override を有効化する。
- `_mainContentUserGestureOverrideEnabled = NO`: main content user gesture override を無効化する。
- Implementation: [`Source/WebCore/html/HTMLMediaElement.cpp#L684`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLMediaElement.cpp#L684) の `MediaElementSession::create` が `mainContentUserGestureOverrideEnabled()` を参照する。

## Details
- WebPreferences key: `MainContentUserGestureOverrideEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L229`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L229)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1229`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1229)
- [`Source/WebCore/html/HTMLMediaElement.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLMediaElement.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4704`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4704) (key: `MainContentUserGestureOverrideEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
