# ``WKInternalsNotes/WKPreferences/_appBadgeEnabled``

App Badge を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAppBadgeEnabled:) BOOL _appBadgeEnabled WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_appBadgeEnabled = YES`: App Badge を有効化する。
- `_appBadgeEnabled = NO`: App Badge を無効化する。
- Implementation: [`NavigatorBadge.idl#L27`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/badge/NavigatorBadge.idl#L27)（`EnabledBySetting=AppBadgeEnabled`）

## Details
- WebPreferences key: `AppBadgeEnabled`

## References
- [`WKPreferencesPrivate.h#L190`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L190)
- [`WKPreferences.mm#L1620`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1620)
- [`NavigatorBadge.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/badge/NavigatorBadge.idl)
- [`UnifiedWebPreferences.yaml#L468`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L468) (key: `AppBadgeEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
