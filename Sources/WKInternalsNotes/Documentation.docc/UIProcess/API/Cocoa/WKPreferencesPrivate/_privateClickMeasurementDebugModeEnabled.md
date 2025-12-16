# ``WKInternalsNotes/WKPreferencesPrivate/_privateClickMeasurementDebugModeEnabled``

Private Click Measurement Debug Mode を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setPrivateClickMeasurementDebugModeEnabled:) BOOL _privateClickMeasurementDebugModeEnabled WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_privateClickMeasurementDebugModeEnabled = YES`: Private Click Measurement Debug Mode を有効化する。
- `_privateClickMeasurementDebugModeEnabled = NO`: Private Click Measurement Debug Mode を無効化する。
- Implementation: [[[`Source/WebKit/NetworkProcess/NetworkSession.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/NetworkProcess/NetworkSession.h)](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/NetworkProcess/NetworkSession.h)](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/NetworkProcess/NetworkSession.h) の `CanMakeCheckedPtr::setDidBeginCheckedPtrDeletion` が `privateClickMeasurementDebugModeEnabled()` を参照する。

## Details
- WebPreferences key: `PrivateClickMeasurementDebugModeEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L174`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L174)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1449`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1449)
- [`Source/WebKit/NetworkProcess/NetworkSession.h#L249`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/NetworkProcess/NetworkSession.h#L249)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6147`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6147) (key: `PrivateClickMeasurementDebugModeEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
