# ``WKInternalsNotes/_WKSystemPreferences/isCaptivePortalModeEnabled()``

Captive Portal Mode が有効かを返す。

## Objective-C Declaration
```objective-c
+ (BOOL)isCaptivePortalModeEnabled;
```

## Discussion
`WKLockdownModeEnabledKey` の設定値を確認し、有効なら `true`。未設定の場合は環境に応じて `PAL::isLockdownModeEnabled()` または `LDMEnabledKey` を参照する。

## References
- [`_WKSystemPreferences.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSystemPreferences.h#L32)
- [`_WKSystemPreferences.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSystemPreferences.mm#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
