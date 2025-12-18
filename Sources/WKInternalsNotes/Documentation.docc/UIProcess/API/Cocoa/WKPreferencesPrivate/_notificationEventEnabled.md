# ``WKInternalsNotes/WKPreferences/_notificationEventEnabled``

NotificationEvent support を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setNotificationEventEnabled:) BOOL _notificationEventEnabled WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Default Value
条件付き: `ENABLE(NOTIFICATION_EVENT) && !PLATFORM(IOS_FAMILY): YES / default: NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_notificationEventEnabled = YES`: NotificationEvent support を有効化する。
- `_notificationEventEnabled = NO`: NotificationEvent support を無効化する。
- Implementation: [`Source/WebCore/Modules/notifications/NotificationEvent.idl#L29`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/notifications/NotificationEvent.idl#L29)（`EnabledBySetting=NotificationEventEnabled`）

## Details
- WebPreferences key: `NotificationEventEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L183`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L183)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1550`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1550)
- [`Source/WebCore/Modules/notifications/NotificationEvent.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/notifications/NotificationEvent.idl)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5602`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5602) (key: `NotificationEventEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
