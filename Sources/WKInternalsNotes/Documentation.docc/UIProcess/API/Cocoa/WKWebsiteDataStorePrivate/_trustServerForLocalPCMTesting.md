# ``WKInternalsNotes/WKWebsiteDataStore/_trustServerForLocalPCMTesting(_:)``

Local PCM テスト用にサーバ証明書を信頼する。

## Objective-C Declaration
```objective-c
- (void)_trustServerForLocalPCMTesting:(SecTrustRef)serverTrust WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`CertificateInfo` に変換して `allowTLSCertificateChainForLocalPCMTesting` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L100)
- [`WKWebsiteDataStore.mm#L1160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1160)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
