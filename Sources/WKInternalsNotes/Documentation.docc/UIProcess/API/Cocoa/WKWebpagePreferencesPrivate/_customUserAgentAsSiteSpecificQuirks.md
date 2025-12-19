# ``WKInternalsNotes/WKWebpagePreferences/_customUserAgentAsSiteSpecificQuirks``

サイト固有互換用の User-Agent を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setCustomUserAgentAsSiteSpecificQuirks:) NSString *_customUserAgentAsSiteSpecificQuirks;
```

## Default Value
初期値は `WebsitePolicies::customUserAgentAsSiteSpecificQuirks()` に依存する。

## Discussion
setter は `setCustomUserAgentAsSiteSpecificQuirks` を呼び、getter は保持されている値を返す。

## References
- [`WKWebpagePreferencesPrivate.h#L107`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L107)
- [`WKWebpagePreferences.mm#L442`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L442)
- [`WKWebpagePreferences.mm#L447`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L447)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
