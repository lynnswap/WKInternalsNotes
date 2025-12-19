# ``WKInternalsNotes/WKWebpagePreferences/_enhancedSecurityEnabled``

強化セキュリティの有効状態を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setEnhancedSecurityEnabled:) BOOL _enhancedSecurityEnabled WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Default Value
初期値は `WebsitePolicies::enhancedSecurityEnabled()` に依存する。

## Discussion
setter は `setEnhancedSecurityEnabled` を呼び、getter は `enhancedSecurityEnabled()` を返す。

## References
- [`WKWebpagePreferencesPrivate.h#L138`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L138)
- [`WKWebpagePreferences.mm#L502`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L502)
- [`WKWebpagePreferences.mm#L507`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L507)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
