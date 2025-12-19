# ``WKInternalsNotes/WKWebsiteDataStore/_setRestrictedOpenerTypeForTesting(_:forDomain:)``

テスト用に Restricted Opener Type を設定する。

## Objective-C Declaration
```objective-c
-(void)_setRestrictedOpenerTypeForTesting:(_WKRestrictedOpenerType)type forDomain:(NSString *)domain WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
`RegistrableDomain` に変換し、`setRestrictedOpenerTypeForDomainForTesting` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L148`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L148)
- [`WKWebsiteDataStore.mm#L1497`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1497)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
