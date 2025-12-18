# ``WKInternalsNotes/WKPreferences/_cookieEnabled``

Cookies を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setCookieEnabled:) BOOL _cookieEnabled WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_cookieEnabled = YES`: Cookies を有効化する。
- `_cookieEnabled = NO`: Cookies を無効化する。
- Implementation: [`Document.cpp#L7175`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp#L7175) の `Document::cookie` が `cookieEnabled()` を参照する。

## Details
- WebPreferences key: `CookieEnabled`

## References
- [`WKPreferencesPrivate.h#L220`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L220)
- [`WKPreferences.mm#L1129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1129)
- [`Document.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp)
- [`UnifiedWebPreferences.yaml#L1994`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L1994) (key: `CookieEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
