# ``WKInternalsNotes/WKPreferences/_topNavigationToDataURLsAllowed``

top navigation to data: URLs を許可/禁止する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setTopNavigationToDataURLsAllowed:) BOOL _topNavigationToDataURLsAllowed WK_API_AVAILABLE(macos(11.0));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_topNavigationToDataURLsAllowed = YES`: top navigation to data: URLs を許可する。
- `_topNavigationToDataURLsAllowed = NO`: top navigation to data: URLs を禁止する。
- Implementation: [`Source/WebCore/loader/DocumentLoader.cpp#L1075`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/loader/DocumentLoader.cpp#L1075) の `DocumentLoader::disallowDataRequest` が `allowTopNavigationToDataURLs()` を参照する。

## Details
- WebPreferences key: `AllowTopNavigationToDataURLs`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L218`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L218)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1109)
- [`Source/WebCore/loader/DocumentLoader.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/loader/DocumentLoader.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L286`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L286) (key: `AllowTopNavigationToDataURLs`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
