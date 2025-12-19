# ``WKInternalsNotes/WKWebpagePreferences/_allowsJSHandleCreationInPageWorld``

ページ world で JSHandle の作成を許可するかを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowsJSHandleCreationInPageWorld:) BOOL _allowsJSHandleCreationInPageWorld WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Default Value
初期値は `WebsitePolicies::allowsJSHandleCreationInPageWorld()` に依存する。

## Discussion
setter は `setAllowsJSHandleCreationInPageWorld` を呼び、getter は `allowsJSHandleCreationInPageWorld()` を返す。

## References
- [`WKWebpagePreferencesPrivate.h#L136`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L136)
- [`WKWebpagePreferences.mm#L826`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L826)
- [`WKWebpagePreferences.mm#L826`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L826)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
