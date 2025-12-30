# ``WKInternalsNotes/_WKSystemPreferences/setCaptivePortalModeEnabled(_:)``

Captive Portal Mode の有効/無効を設定する。

## Objective-C Declaration
```objective-c
+ (void)setCaptivePortalModeEnabled:(BOOL)enabled;
```

## Discussion
設定値を `CFPreferencesSetValue` で更新し同期した後、Darwin 通知で設定変更を通知する。

## References
- [`_WKSystemPreferences.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSystemPreferences.h#L33)
- [`_WKSystemPreferences.mm#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSystemPreferences.mm#L55)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
