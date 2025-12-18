# ``WKInternalsNotes/WKPreferences/_invisibleMediaAutoplayNotPermitted``

Invisible Autoplay Not Permitted を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setInvisibleMediaAutoplayNotPermitted:) BOOL _invisibleMediaAutoplayNotPermitted WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_invisibleMediaAutoplayNotPermitted = YES`: Invisible Autoplay Not Permitted を有効化する。
- `_invisibleMediaAutoplayNotPermitted = NO`: Invisible Autoplay Not Permitted を無効化する。
- Implementation: [`HTMLMediaElement.cpp#L684`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLMediaElement.cpp#L684) の `MediaElementSession::create` が `invisibleAutoplayNotPermitted()` を参照する。

## Details
- WebPreferences key: `InvisibleAutoplayNotPermitted`

## References
- [`WKPreferencesPrivate.h#L227`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L227)
- [`WKPreferences.mm#L1209`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1209)
- [`HTMLMediaElement.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLMediaElement.cpp)
- [`UnifiedWebPreferences.yaml#L4049`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4049) (key: `InvisibleAutoplayNotPermitted`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
