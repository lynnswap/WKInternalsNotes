# ``WKInternalsNotes/WKProcessPool/_setAllowsSpecificHTTPSCertificate(_:forHost:)``

特定の HTTPS 証明書チェーンをホストに許可する。

## Objective-C Declaration
```objective-c
- (void)_setAllowsSpecificHTTPSCertificate:(NSArray *)certificateChain forHost:(NSString *)host WK_API_DEPRECATED_WITH_REPLACEMENT("WKWebsiteDataStore._allowTLSCertificateChain:forHost:", macos(10.10, 12.0), ios(8.0, 15.0));
```

## Discussion
現在の実装は空で、処理は行わない。

## References
- [`WKProcessPoolPrivate.h#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L85)
- [`WKProcessPool.mm#L229`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L229)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
