# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/allowsHSTSWithUntrustedRootCertificate``

信頼されていないルート証明書で HSTS を許可するかを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL allowsHSTSWithUntrustedRootCertificate WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `allowsHSTSWithUntrustedRootCertificate` の値を返す。

## Discussion
getter は `_configuration->allowsHSTSWithUntrustedRootCertificate()` を返し、setter は `_configuration->setAllowsHSTSWithUntrustedRootCertificate` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L94](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L94)
- [_WKWebsiteDataStoreConfiguration.mm#L786](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L786)
- [_WKWebsiteDataStoreConfiguration.mm#L791](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L791)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
