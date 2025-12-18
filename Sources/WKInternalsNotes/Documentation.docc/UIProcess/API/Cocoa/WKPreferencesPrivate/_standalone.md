# ``WKInternalsNotes/WKPreferences/_standalone``

Standalone を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setStandalone:, getter=_isStandalone) BOOL _standalone WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_standalone = YES`: Standalone を有効化する。
- `_standalone = NO`: Standalone を無効化する。
- Implementation: [`Navigator.cpp#L356`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/Navigator.cpp#L356) の `Navigator::standalone` が `standalone()` を参照する。

## Details
- WebPreferences key: `Standalone`

## References
- [`WKPreferencesPrivate.h#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L99)
- [`WKPreferences.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm)
- [`Navigator.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/Navigator.cpp)
- [`UnifiedWebPreferences.yaml#L7613`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7613) (key: `Standalone`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
