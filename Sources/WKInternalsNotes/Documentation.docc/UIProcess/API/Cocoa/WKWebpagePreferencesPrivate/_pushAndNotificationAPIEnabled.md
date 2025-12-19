# ``WKInternalsNotes/WKWebpagePreferences/_pushAndNotificationAPIEnabled``

Push/Notification API の有効状態を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setPushAndNotificationAPIEnabled:) BOOL _pushAndNotificationAPIEnabled;
```

## Default Value
初期値は `pushAndNotificationsEnabledPolicy()` の状態に依存する。

## Discussion
getter は policy が `Yes` かどうかで判定し、setter は `Yes`/`No` を設定する。

## References
- [`WKWebpagePreferencesPrivate.h#L132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L132)
- [`WKWebpagePreferences.mm#L800`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L800)
- [`WKWebpagePreferences.mm#L805`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L805)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
