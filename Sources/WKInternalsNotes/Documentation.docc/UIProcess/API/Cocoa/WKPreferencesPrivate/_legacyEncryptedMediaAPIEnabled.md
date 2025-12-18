# ``WKInternalsNotes/WKPreferences/_legacyEncryptedMediaAPIEnabled``

legacy EME API を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setLegacyEncryptedMediaAPIEnabled:) BOOL _legacyEncryptedMediaAPIEnabled WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_legacyEncryptedMediaAPIEnabled = YES`: legacy EME API を有効化する。
- `_legacyEncryptedMediaAPIEnabled = NO`: legacy EME API を無効化する。
- Implementation: [`WebKitMediaKeyMessageEvent.idl#L28`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/encryptedmedia/legacy/WebKitMediaKeyMessageEvent.idl#L28)（`EnabledBySetting=LegacyEncryptedMediaAPIEnabled`）

## Details
- WebPreferences key: `LegacyEncryptedMediaAPIEnabled`

## References
- [`WKPreferencesPrivate.h#L228`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L228)
- [`WKPreferences.mm#L1219`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1219)
- [`WebKitMediaKeyMessageEvent.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/encryptedmedia/legacy/WebKitMediaKeyMessageEvent.idl)
- [`UnifiedWebPreferences.yaml#L4353`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4353) (key: `LegacyEncryptedMediaAPIEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
