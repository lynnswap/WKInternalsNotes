# ``WKInternalsNotes/WKPreferences/_notificationsEnabled``

Notifications を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setNotificationsEnabled:) BOOL _notificationsEnabled WK_API_AVAILABLE(macos(10.13.4), ios(16.0));
```

## Default Value
iOS: `NO` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_notificationsEnabled = YES`: Notifications を有効化する。
- `_notificationsEnabled = NO`: Notifications を無効化する。
- Implementation: [`Notification.idl#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/notifications/Notification.idl#L37)（`EnabledBySetting=NotificationsEnabled`）

## Details
- WebPreferences key: `NotificationsEnabled`

## References
- [`WKPreferencesPrivate.h#L182`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L182)
- [`WKPreferences.mm#L1540`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1540)
- [`Notification.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/notifications/Notification.idl)
- [`UnifiedWebPreferences.yaml#L5619`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5619) (key: `NotificationsEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
