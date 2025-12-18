# ``WKInternalsNotes/WKPreferences/_accessibilityIsolatedTreeEnabled``

Isolated Accessibility Tree Mode を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAccessibilityIsolatedTreeEnabled:) BOOL _accessibilityIsolatedTreeEnabled WK_API_AVAILABLE(macos(10.16));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_accessibilityIsolatedTreeEnabled = YES`: Isolated Accessibility Tree Mode を有効化する。
- `_accessibilityIsolatedTreeEnabled = NO`: Isolated Accessibility Tree Mode を無効化する。
- Implementation: [`Source/WebCore/page/DeprecatedGlobalSettings.h#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/DeprecatedGlobalSettings.h#L103) で `isAccessibilityIsolatedTreeEnabled()` が参照される。

## Details
- WebPreferences key: `IsAccessibilityIsolatedTreeEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L171`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L171)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1420`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1420)
- [`Source/WebCore/page/DeprecatedGlobalSettings.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/DeprecatedGlobalSettings.h)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4062`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4062) (key: `IsAccessibilityIsolatedTreeEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
