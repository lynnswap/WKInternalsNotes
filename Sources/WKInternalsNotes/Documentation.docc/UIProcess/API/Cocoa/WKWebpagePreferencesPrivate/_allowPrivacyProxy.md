# ``WKInternalsNotes/WKWebpagePreferences/_allowPrivacyProxy``

Privacy Proxy の利用可否を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowPrivacyProxy:) BOOL _allowPrivacyProxy WK_API_AVAILABLE(macos(13.1), ios(16.2));
```

## Default Value
初期値は `WebsitePolicies::allowPrivacyProxy()` に依存する。

## Discussion
setter は `setAllowPrivacyProxy` を呼び、getter は `allowPrivacyProxy()` を返す。

## References
- [`WKWebpagePreferencesPrivate.h#L118`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L118)
- [`WKWebpagePreferences.mm#L528`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L528)
- [`WKWebpagePreferences.mm#L533`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L533)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
