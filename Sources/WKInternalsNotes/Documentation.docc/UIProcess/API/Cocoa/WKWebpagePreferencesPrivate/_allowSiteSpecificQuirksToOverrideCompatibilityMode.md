# ``WKInternalsNotes/WKWebpagePreferences/_allowSiteSpecificQuirksToOverrideCompatibilityMode``

サイト固有 quirks が互換モードを上書きできるかを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowSiteSpecificQuirksToOverrideCompatibilityMode:) BOOL _allowSiteSpecificQuirksToOverrideCompatibilityMode;
```

## Default Value
初期値は `WebsitePolicies::allowSiteSpecificQuirksToOverrideContentMode()` に依存する。

## Discussion
getter は `allowSiteSpecificQuirksToOverrideContentMode()` を返し、setter は同値を設定する。

## References
- [`WKWebpagePreferencesPrivate.h#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L110)
- [`WKWebpagePreferences.mm#L462`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L462)
- [`WKWebpagePreferences.mm#L462`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L462)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
