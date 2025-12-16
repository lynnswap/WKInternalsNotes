# ``WKInternalsNotes/WKPreferencesPrivate/_resourceUsageOverlayVisible``

Resource usage overlay を表示/非表示にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setResourceUsageOverlayVisible:) BOOL _resourceUsageOverlayVisible WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_resourceUsageOverlayVisible = YES`: Resource usage overlay を表示する。
- `_resourceUsageOverlayVisible = NO`: Resource usage overlay を非表示にする。
- Implementation: [`Source/WebCore/page/SettingsBase.cpp#L528`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/SettingsBase.cpp#L528) の `SettingsBase::resourceUsageOverlayVisibleChanged` が `resourceUsageOverlayVisible()` を参照する。

## Details
- WebPreferences key: `ResourceUsageOverlayVisible`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L78)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L346`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L346)
- [`Source/WebCore/page/SettingsBase.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/SettingsBase.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6510`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6510) (key: `ResourceUsageOverlayVisible`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
