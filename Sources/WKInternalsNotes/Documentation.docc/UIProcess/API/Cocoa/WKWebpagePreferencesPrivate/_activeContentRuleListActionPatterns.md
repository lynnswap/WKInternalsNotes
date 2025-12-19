# ``WKInternalsNotes/WKWebpagePreferences/_activeContentRuleListActionPatterns``

有効な content rule list の action pattern を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setActiveContentRuleListActionPatterns:) NSDictionary<NSString *, NSSet<NSString *> *> *_activeContentRuleListActionPatterns WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
初期値は `API::WebsitePolicies` が保持する action pattern の状態に依存する。

## Discussion
setter は NSDictionary/NSSet を HashMap<String, Vector<String>> に変換して保持する。getter は保持しているパターンを NSDictionary/NSSet として再構築する。

## References
- [`WKWebpagePreferencesPrivate.h#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L99)
- [`WKWebpagePreferences.mm#L225`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L225)
- [`WKWebpagePreferences.mm#L238`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L238)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
