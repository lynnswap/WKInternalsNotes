# ``WKInternalsNotes/WKPreferencesPrivate/_universalAccessFromFileURLsAllowed``

universal access from file: URLs を許可/禁止する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setUniversalAccessFromFileURLsAllowed:) BOOL _universalAccessFromFileURLsAllowed WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_universalAccessFromFileURLsAllowed = YES`: universal access from file: URLs を許可する。
- `_universalAccessFromFileURLsAllowed = NO`: universal access from file: URLs を禁止する。
- Implementation: [`Source/WebCore/dom/Document.cpp#L8359`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp#L8359) の `SecurityOriginPolicy::create` が `allowUniversalAccessFromFileURLs()` を参照する。

## Details
- WebPreferences key: `AllowUniversalAccessFromFileURLs`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L217`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L217)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1099`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1099)
- [`Source/WebCore/dom/Document.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L298`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L298) (key: `AllowUniversalAccessFromFileURLs`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
