# ``WKInternalsNotes/WKPreferencesPrivate/_applePayEnabled``

Apple Pay を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setApplePayEnabled:) BOOL _applePayEnabled WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_applePayEnabled = YES`: Apple Pay を有効化する。
- `_applePayEnabled = NO`: Apple Pay を無効化する。
- Implementation: [`Source/WebCore/Modules/applepay/ApplePaySession.idl#L29`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/applepay/ApplePaySession.idl#L29)（`EnabledBySetting=ApplePayEnabled`）

## Details
- WebPreferences key: `ApplePayEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L225`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L225)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1189`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1189)
- [`Source/WebCore/Modules/applepay/ApplePaySession.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/applepay/ApplePaySession.idl)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L525`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L525) (key: `ApplePayEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
