# ``WKInternalsNotes/WKPreferences/_serviceWorkerEntitlementDisabledForTesting``

Service Worker Entitlement をテスト用に無効化する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setServiceWorkerEntitlementDisabledForTesting:) BOOL _serviceWorkerEntitlementDisabledForTesting WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_serviceWorkerEntitlementDisabledForTesting = YES`: Service Worker Entitlement をテスト用に無効化する。
- `_serviceWorkerEntitlementDisabledForTesting = NO`: Service Worker Entitlement を無効化しない。
- Implementation: [`Source/WebKit/UIProcess/WebPageProxy.cpp#L915`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp#L915) の `DeprecatedGlobalSettings::setDisableScreenSizeOverride` が `serviceWorkerEntitlementDisabledForTesting()` を参照する。

## Details
- WebPreferences key: `ServiceWorkerEntitlementDisabledForTesting`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L170`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L170)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L993`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L993)
- [`Source/WebKit/UIProcess/WebPageProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6963`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6963) (key: `ServiceWorkerEntitlementDisabledForTesting`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
