# ``WKInternalsNotes/_WKSystemPreferences/isCaptivePortalModeIgnored(_:)``

特定コンテナで Captive Portal Mode を無視するかを返す。

## Objective-C Declaration
```objective-c
+ (BOOL)isCaptivePortalModeIgnored:(NSString *)containerPath;
```

## Discussion
`PLATFORM(IOS_FAMILY)` では `System/Preferences/` 配下の ignore ファイル有無で判定する。その他プラットフォームでは `false`。

## References
- [`_WKSystemPreferences.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSystemPreferences.h#L34)
- [`_WKSystemPreferences.mm#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSystemPreferences.mm#L62)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
