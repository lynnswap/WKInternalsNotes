# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/requiresSecureHTTPSProxyConnection``

HTTPS プロキシ接続のセキュア要求を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL requiresSecureHTTPSProxyConnection WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `requiresSecureHTTPSProxyConnection` の値を返す。

## Discussion
getter は `_configuration->requiresSecureHTTPSProxyConnection()` を返し、setter は `_configuration->setRequiresSecureHTTPSProxyConnection` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L65](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L65)
- [_WKWebsiteDataStoreConfiguration.mm#L721](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L721)
- [_WKWebsiteDataStoreConfiguration.mm#L726](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L726)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
