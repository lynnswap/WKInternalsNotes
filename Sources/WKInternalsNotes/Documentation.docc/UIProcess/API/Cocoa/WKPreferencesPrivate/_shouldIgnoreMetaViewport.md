# ``WKInternalsNotes/WKPreferences/_shouldIgnoreMetaViewport``

Ignore Meta Viewport を切り替える API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setShouldIgnoreMetaViewport:) BOOL _shouldIgnoreMetaViewport WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_shouldIgnoreMetaViewport = YES`: Ignore Meta Viewport を有効化する。
- `_shouldIgnoreMetaViewport = NO`: Ignore Meta Viewport を無効化する。
- Implementation: [`WebPage.cpp#L532`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/WebProcess/WebPage/WebPage.cpp#L532) の `WebProcess::singleton` が `shouldIgnoreMetaViewport()` を参照する。

## Details
- WebPreferences key: `ShouldIgnoreMetaViewport`

## References
- [`WKPreferencesPrivate.h#L160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L160)
- [`WKPreferences.mm#L888`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L888)
- [`WebPage.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/WebProcess/WebPage/WebPage.cpp)
- [`UnifiedWebPreferences.yaml#L7236`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7236) (key: `ShouldIgnoreMetaViewport`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
