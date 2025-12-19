# ``WKInternalsNotes/WKWebsiteDataStore/_allowTLSCertificateChain(_:forHost:)``

指定ホストの TLS 証明書チェーンを許可する。

## Objective-C Declaration
```objective-c
- (void)_allowTLSCertificateChain:(NSArray *)certificateChain forHost:(NSString *)host WK_API_DEPRECATED_WITH_REPLACEMENT("WKNavigationDelegate.didReceiveAuthenticationChallenge", macos(12.0, 14.2), ios(15.0, 17.2));
```

## Discussion
現行実装では空実装。

## References
- [`WKWebsiteDataStorePrivate.h#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L99)
- [`WKWebsiteDataStore.mm#L1156`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1156)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
