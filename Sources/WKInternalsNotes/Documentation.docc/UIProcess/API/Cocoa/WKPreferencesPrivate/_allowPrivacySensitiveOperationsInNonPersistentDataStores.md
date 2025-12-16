# ``WKInternalsNotes/WKPreferencesPrivate/_allowPrivacySensitiveOperationsInNonPersistentDataStores``

Privacy-Sensitive Operations in Non-Persistent Data Stores を許可/禁止する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowPrivacySensitiveOperationsInNonPersistentDataStores:) BOOL _allowPrivacySensitiveOperationsInNonPersistentDataStores WK_API_AVAILABLE(macos(15.2), ios(18.2), visionos(2.2));
```

## Default Value
iOS: `NO` / macOS: `NO` / visionOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_allowPrivacySensitiveOperationsInNonPersistentDataStores = YES`: Privacy-Sensitive Operations in Non-Persistent Data Stores を許可する。
- `_allowPrivacySensitiveOperationsInNonPersistentDataStores = NO`: Privacy-Sensitive Operations in Non-Persistent Data Stores を禁止する。
- Implementation: [`Source/WebCore/Modules/webaudio/AudioContext.cpp#L572`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/webaudio/AudioContext.cpp#L572) の `MediaPlayer::invalidTime` が `allowPrivacySensitiveOperationsInNonPersistentDataStores()` を参照する。

## Details
- WebPreferences key: `AllowPrivacySensitiveOperationsInNonPersistentDataStores`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L196`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L196)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1650`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1650)
- [`Source/WebCore/Modules/webaudio/AudioContext.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/webaudio/AudioContext.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L262`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L262) (key: `AllowPrivacySensitiveOperationsInNonPersistentDataStores`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
