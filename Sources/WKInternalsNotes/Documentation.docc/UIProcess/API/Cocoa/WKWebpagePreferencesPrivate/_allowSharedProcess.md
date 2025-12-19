# ``WKInternalsNotes/WKWebpagePreferences/_allowSharedProcess``

共有プロセスの利用を許可するかを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowSharedProcess:) BOOL _allowSharedProcess WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Default Value
初期値は `WebsitePolicies::allowSharedProcess()` に依存する。

## Discussion
getter は `allowSharedProcess()` を返し、setter は同値を設定する。

## References
- [`WKWebpagePreferencesPrivate.h#L128`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L128)
- [`WKWebpagePreferences.mm#L790`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L790)
- [`WKWebpagePreferences.mm#L790`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L790)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
