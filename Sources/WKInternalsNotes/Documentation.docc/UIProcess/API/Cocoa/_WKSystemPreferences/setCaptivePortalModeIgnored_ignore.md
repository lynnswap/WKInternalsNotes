# ``WKInternalsNotes/_WKSystemPreferences/setCaptivePortalModeIgnored(_:ignore:)``

特定コンテナで Captive Portal Mode を無視する設定を更新する。

## Objective-C Declaration
```objective-c
+ (void)setCaptivePortalModeIgnored:(NSString *)containerPath ignore:(BOOL)ignore;
```

## Discussion
`PLATFORM(IOS_FAMILY)` でのみ動作。ignore ファイルの作成/削除を行い、Darwin 通知で設定変更を通知する。

## References
- [`_WKSystemPreferences.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSystemPreferences.h#L35)
- [`_WKSystemPreferences.mm#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSystemPreferences.mm#L71)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
