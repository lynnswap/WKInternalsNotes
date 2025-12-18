# ``WKInternalsNotes/WKPreferences/_applePayCapabilityDisclosureAllowed``

Apple Pay Capability Disclosure を許可/禁止する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setApplePayCapabilityDisclosureAllowed:) BOOL _applePayCapabilityDisclosureAllowed WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_applePayCapabilityDisclosureAllowed = YES`: Apple Pay Capability Disclosure を許可する。
- `_applePayCapabilityDisclosureAllowed = NO`: Apple Pay Capability Disclosure を禁止する。
- Implementation: [`ApplePaySession.cpp#L517`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/applepay/ApplePaySession.cpp#L517) の `ApplePaySession::supportsVersion` が `applePayCapabilityDisclosureAllowed()` を参照する。

## Details
- WebPreferences key: `ApplePayCapabilityDisclosureAllowed`

## References
- [`WKPreferencesPrivate.h#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L111)
- [`WKPreferences.mm#L614`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L614)
- [`ApplePaySession.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/applepay/ApplePaySession.cpp)
- [`UnifiedWebPreferences.yaml#L512`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L512) (key: `ApplePayCapabilityDisclosureAllowed`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
