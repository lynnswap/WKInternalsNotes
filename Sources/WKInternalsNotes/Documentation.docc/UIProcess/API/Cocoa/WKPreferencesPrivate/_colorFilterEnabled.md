# ``WKInternalsNotes/WKPreferences/_colorFilterEnabled``

Color Filter を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setColorFilterEnabled:) BOOL _colorFilterEnabled WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_colorFilterEnabled = YES`: CSS `-apple-color-filter` が有効になり、宣言が解釈される。
- `_colorFilterEnabled = NO`: CSS `-apple-color-filter` が無効になり、宣言が解釈されない。
- Implementation: [`Source/WebCore/css/CSSProperties.json#L9348`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/css/CSSProperties.json#L9348) の `-apple-color-filter` が `settings-flag: colorFilterEnabled` で gated される。

## Details
- WebPreferences key: `ColorFilterEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L157`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L157)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L858`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L858)
- [`Source/WebCore/css/CSSProperties.json`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/css/CSSProperties.json)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L1829`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L1829) (key: `ColorFilterEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
