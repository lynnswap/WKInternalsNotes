# ``WKInternalsNotes/WKPreferences/_itpDebugModeEnabled``

ITP Debug Mode を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setItpDebugModeEnabled:) BOOL _itpDebugModeEnabled WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_itpDebugModeEnabled = YES`: ITP Debug Mode を有効化する。
- `_itpDebugModeEnabled = NO`: ITP Debug Mode を無効化する。
- Implementation: Web Inspector は `ITPDebugModeEnabled` を developer preference として扱い、`InspectorPageAgent` 経由で override を設定する（[`InspectorPageAgent.cpp#L172`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/inspector/agents/InspectorPageAgent.cpp#L172)）。

## Details
- WebPreferences key: `ItpDebugModeEnabled`

## References
- [`WKPreferencesPrivate.h#L164`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L164)
- [`WKPreferences.mm#L908`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L908)
- [`InspectorPageAgent.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/inspector/agents/InspectorPageAgent.cpp)
- [`UnifiedWebPreferences.yaml#L4168`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4168) (key: `ItpDebugModeEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
