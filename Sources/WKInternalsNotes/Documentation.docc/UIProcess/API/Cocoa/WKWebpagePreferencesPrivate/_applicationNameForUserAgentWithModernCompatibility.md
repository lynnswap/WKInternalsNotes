# ``WKInternalsNotes/WKWebpagePreferences/_applicationNameForUserAgentWithModernCompatibility``

モダン互換 UA 用の applicationName を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setApplicationNameForUserAgentWithModernCompatibility:) NSString *_applicationNameForUserAgentWithModernCompatibility;
```

## Default Value
初期値は `WebsitePolicies::applicationNameForDesktopUserAgent()` に依存する。

## Discussion
getter は `applicationNameForDesktopUserAgent()` を返し、setter は同値を設定する。

## References
- [`WKWebpagePreferencesPrivate.h#L112`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L112)
- [`WKWebpagePreferences.mm#L472`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L472)
- [`WKWebpagePreferences.mm#L472`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L472)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
