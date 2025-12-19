# ``WKInternalsNotes/WKWebpagePreferences/_customUserAgent``

カスタム User-Agent を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setCustomUserAgent:) NSString *_customUserAgent;
```

## Default Value
初期値は `WebsitePolicies::customUserAgent()` に依存する。

## Discussion
setter は `setCustomUserAgent` を呼び、getter は保持されている User-Agent を返す。

## References
- [`WKWebpagePreferencesPrivate.h#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L106)
- [`WKWebpagePreferences.mm#L432`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L432)
- [`WKWebpagePreferences.mm#L437`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L437)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
