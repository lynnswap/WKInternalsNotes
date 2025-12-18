# ``WKInternalsNotes/WKPreferences/_needsInAppBrowserPrivacyQuirks``

Needs In-App Browser Privacy Quirks を切り替える API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setNeedsInAppBrowserPrivacyQuirks:) BOOL _needsInAppBrowserPrivacyQuirks WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_needsInAppBrowserPrivacyQuirks = YES`: Needs In-App Browser Privacy Quirks を有効化する。
- `_needsInAppBrowserPrivacyQuirks = NO`: Needs In-App Browser Privacy Quirks を無効化する。
- Implementation: [`Source/WebKit/WebProcess/WebPage/WebFrame.cpp#L1293`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/WebProcess/WebPage/WebFrame.cpp#L1293) の `WebFrame::shouldEnableInAppBrowserPrivacyProtections` が `needsInAppBrowserPrivacyQuirks()` を参照する。

## Details
- WebPreferences key: `NeedsInAppBrowserPrivacyQuirks`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L84)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L406`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L406)
- [`Source/WebKit/WebProcess/WebPage/WebFrame.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/WebProcess/WebPage/WebFrame.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5545`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5545) (key: `NeedsInAppBrowserPrivacyQuirks`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
