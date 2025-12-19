# ``WKInternalsNotes/WKWebpagePreferences/_colorSchemePreference``

色スキームの上書き設定を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setColorSchemePreference:) _WKWebsiteColorSchemePreference _colorSchemePreference;
```

## Default Value
初期値は `WebsitePolicies::colorSchemePreference()` に依存する。

## Discussion
getter は `ColorSchemePreference` を `_WKWebsiteColorSchemePreference` に変換して返す。setter は逆変換して設定する。

## References
- [`WKWebpagePreferencesPrivate.h#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L120)
- [`WKWebpagePreferences.mm#L538`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L538)
- [`WKWebpagePreferences.mm#L550`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L550)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
