# ``WKInternalsNotes/WKPreferences/_authorAndUserStylesEnabled``

Author And User Styles を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAuthorAndUserStylesEnabled:) BOOL _authorAndUserStylesEnabled WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_authorAndUserStylesEnabled = YES`: Author And User Styles を有効化する。
- `_authorAndUserStylesEnabled = NO`: Author And User Styles を無効化する。
- Implementation: [`Source/WebCore/style/StyleResolver.cpp#L177`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/style/StyleResolver.cpp#L177) の `Resolver::Resolver` が `authorAndUserStylesEnabled()` を参照する。

## Details
- WebPreferences key: `AuthorAndUserStylesEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L210`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L210)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1029`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1029)
- [`Source/WebCore/style/StyleResolver.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/style/StyleResolver.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L663`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L663) (key: `AuthorAndUserStylesEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
