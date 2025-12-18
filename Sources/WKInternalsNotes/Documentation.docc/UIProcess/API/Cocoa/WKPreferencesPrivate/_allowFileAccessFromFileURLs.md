# ``WKInternalsNotes/WKPreferences/_allowFileAccessFromFileURLs``

File Access From File URLs を許可/禁止する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowFileAccessFromFileURLs:) BOOL _allowFileAccessFromFileURLs WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_allowFileAccessFromFileURLs = YES`: File Access From File URLs を許可する。
- `_allowFileAccessFromFileURLs = NO`: File Access From File URLs を禁止する。
- Implementation: [`Document.cpp#L8359`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp#L8359) の `SecurityOriginPolicy::create` が `allowFileAccessFromFileURLs()` を参照する。

## Details
- WebPreferences key: `AllowFileAccessFromFileURLs`

## References
- [`WKPreferencesPrivate.h#L96`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L96)
- [`WKPreferences.mm#L486`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L486)
- [`Document.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp)
- [`UnifiedWebPreferences.yaml#L225`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L225) (key: `AllowFileAccessFromFileURLs`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
