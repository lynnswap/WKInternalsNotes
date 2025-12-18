# ``WKInternalsNotes/WKPreferences/_appNapEnabled``

page visibility-based process suppression を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAppNapEnabled:) BOOL _appNapEnabled WK_API_AVAILABLE(macos(10.15));
```

## Default Value
macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_appNapEnabled = YES`: page visibility-based process suppression を有効化する。
- `_appNapEnabled = NO`: page visibility-based process suppression を無効化する。
- Implementation: [`WebPageProxy.cpp#L3302`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp#L3302) の `WebPageProxy::updateThrottleState` が `pageVisibilityBasedProcessSuppressionEnabled()` を参照する。

## Details
- WebPreferences key: `PageVisibilityBasedProcessSuppressionEnabled`

## References
- [`WKPreferencesPrivate.h#L240`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L240)
- [`WKPreferences.mm#L1339`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1339)
- [`WebPageProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp)
- [`UnifiedWebPreferences.yaml#L5846`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5846) (key: `PageVisibilityBasedProcessSuppressionEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
