# ``WKInternalsNotes/WKPreferences/_privateClickMeasurementEnabled``

Private Click Measurement を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setPrivateClickMeasurementEnabled:) BOOL _privateClickMeasurementEnabled WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_privateClickMeasurementEnabled = YES`: Private Click Measurement を有効化する。
- `_privateClickMeasurementEnabled = NO`: Private Click Measurement を無効化する。
- Implementation: [`HTMLAnchorElement.idl#L24`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLAnchorElement.idl#L24)（`EnabledBySetting=PrivateClickMeasurementEnabled`）

## Details
- WebPreferences key: `PrivateClickMeasurementEnabled`

## References
- [`WKPreferencesPrivate.h#L173`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L173)
- [`WKPreferences.mm#L1439`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1439)
- [`HTMLAnchorElement.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLAnchorElement.idl)
- [`UnifiedWebPreferences.yaml#L6161`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6161) (key: `PrivateClickMeasurementEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
