# ``WKInternalsNotes/WKWebpagePreferences/_userContentController``

ページに適用する UserContentController を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong, setter=_setUserContentController:) WKUserContentController *_userContentController WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
初期値は `WebsitePolicies::userContentController()` に依存する。

## Discussion
getter は `userContentController()` をラップして返す。setter は `WKUserContentController` の proxy を渡して設定する。

## References
- [`WKWebpagePreferencesPrivate.h#L105`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L105)
- [`WKWebpagePreferences.mm#L422`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L422)
- [`WKWebpagePreferences.mm#L422`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L422)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
