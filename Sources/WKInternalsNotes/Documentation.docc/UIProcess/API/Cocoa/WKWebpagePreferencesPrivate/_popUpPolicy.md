# ``WKInternalsNotes/WKWebpagePreferences/_popUpPolicy``

ポップアップの許可ポリシーを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setPopUpPolicy:) _WKWebsitePopUpPolicy _popUpPolicy;
```

## Default Value
初期値は `WebsitePolicies::popUpPolicy()` に依存する。

## Discussion
setter は `_WKWebsitePopUpPolicy` を `WebsitePopUpPolicy` に変換して設定する。getter は逆変換して返す。

## References
- [`WKWebpagePreferencesPrivate.h#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L103)
- [`WKWebpagePreferences.mm#L384`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L384)
- [`WKWebpagePreferences.mm#L384`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L384)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
