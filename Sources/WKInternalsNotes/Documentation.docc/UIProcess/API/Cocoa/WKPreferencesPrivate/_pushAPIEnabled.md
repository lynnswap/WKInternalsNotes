# ``WKInternalsNotes/WKPreferences/_pushAPIEnabled``

Push API を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setPushAPIEnabled:) BOOL _pushAPIEnabled WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_pushAPIEnabled = YES`: Push API を有効化する。
- `_pushAPIEnabled = NO`: Push API を無効化する。
- Implementation: [`PushEvent.idl#L27`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/push-api/PushEvent.idl#L27)（`EnabledBySetting=PushAPIEnabled`）

## Details
- WebPreferences key: `PushAPIEnabled`

## References
- [`WKPreferencesPrivate.h#L184`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L184)
- [`WKPreferences.mm#L1555`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1555)
- [`PushEvent.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/push-api/PushEvent.idl)
- [`UnifiedWebPreferences.yaml#L6243`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6243) (key: `PushAPIEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
