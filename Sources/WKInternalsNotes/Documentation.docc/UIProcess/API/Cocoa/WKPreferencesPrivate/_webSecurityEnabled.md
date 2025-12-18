# ``WKInternalsNotes/WKPreferences/_webSecurityEnabled``

Web Security を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setWebSecurityEnabled:) BOOL _webSecurityEnabled WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_webSecurityEnabled = YES`: Web Security を有効化する。
- `_webSecurityEnabled = NO`: Web Security を無効化する。
- Implementation: [`Source/WebCore/dom/Document.cpp#L8359`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp#L8359) の `SecurityOriginPolicy::create` が `webSecurityEnabled()` を参照する。

## Details
- WebPreferences key: `WebSecurityEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L216`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L216)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1089`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1089)
- [`Source/WebCore/dom/Document.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L9539`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L9539) (key: `WebSecurityEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
