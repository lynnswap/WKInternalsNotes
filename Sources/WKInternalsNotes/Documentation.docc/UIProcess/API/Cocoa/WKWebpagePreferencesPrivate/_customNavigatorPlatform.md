# ``WKInternalsNotes/WKWebpagePreferences/_customNavigatorPlatform``

navigator.platform の上書き値を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setCustomNavigatorPlatform:) NSString *_customNavigatorPlatform;
```

## Default Value
初期値は `WebsitePolicies::customNavigatorPlatform()` に依存する。

## Discussion
setter は `setCustomNavigatorPlatform` を呼び、getter は保持されている値を返す。

## References
- [`WKWebpagePreferencesPrivate.h#L108`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L108)
- [`WKWebpagePreferences.mm#L457`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L457)
- [`WKWebpagePreferences.mm#L457`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L457)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
