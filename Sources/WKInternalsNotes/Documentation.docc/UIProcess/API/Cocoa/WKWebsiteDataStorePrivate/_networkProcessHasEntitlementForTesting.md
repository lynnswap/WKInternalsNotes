# ``WKInternalsNotes/WKWebsiteDataStore/_networkProcessHasEntitlementForTesting(_:)``

NetworkProcess が指定 entitlements を持つか確認する。

## Objective-C Declaration
```objective-c
- (BOOL)_networkProcessHasEntitlementForTesting:(NSString *)entitlement WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`networkProcessHasEntitlementForTesting` の結果を返す。

## References
- [`WKWebsiteDataStorePrivate.h#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L106)
- [`WKWebsiteDataStore.mm#L1117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1117)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
