# ``WKInternalsNotes/WKPreferencesPrivate/_pageVisibilityBasedProcessSuppressionEnabled``

page visibility-based process suppression を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setPageVisibilityBasedProcessSuppressionEnabled:) BOOL _pageVisibilityBasedProcessSuppressionEnabled WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_pageVisibilityBasedProcessSuppressionEnabled = YES`: page visibility-based process suppression を有効化する。
- `_pageVisibilityBasedProcessSuppressionEnabled = NO`: page visibility-based process suppression を無効化する。
- Implementation: [`Source/WebKit/UIProcess/WebPageProxy.cpp#L3302`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp#L3302) の `WebPageProxy::updateThrottleState` が `pageVisibilityBasedProcessSuppressionEnabled()` を参照する。

## Details
- WebPreferences key: `PageVisibilityBasedProcessSuppressionEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L94`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L94)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L476`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L476)
- [`Source/WebKit/UIProcess/WebPageProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5846`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5846) (key: `PageVisibilityBasedProcessSuppressionEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
