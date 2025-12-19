# ``WKInternalsNotes/WKWebpagePreferences/_autoplayPolicy``

autoplay ポリシーを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAutoplayPolicy:) _WKWebsiteAutoplayPolicy _autoplayPolicy;
```

## Default Value
初期値は `WebsitePolicies::autoplayPolicy()` に依存する。

## Discussion
setter は `_WKWebsiteAutoplayPolicy` を `WebsiteAutoplayPolicy` にマップして設定する。getter は逆変換して返す。

## References
- [`WKWebpagePreferencesPrivate.h#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L101)
- [`WKWebpagePreferences.mm#L289`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L289)
- [`WKWebpagePreferences.mm#L307`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L307)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
