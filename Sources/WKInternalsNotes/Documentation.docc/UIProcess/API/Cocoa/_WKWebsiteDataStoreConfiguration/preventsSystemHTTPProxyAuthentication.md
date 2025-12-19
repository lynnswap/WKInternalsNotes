# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/preventsSystemHTTPProxyAuthentication``

システム HTTP プロキシ認証を抑止するかを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL preventsSystemHTTPProxyAuthentication WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `preventsSystemHTTPProxyAuthentication` の値を返す。

## Discussion
getter は `_configuration->preventsSystemHTTPProxyAuthentication()` を返し、setter は `_configuration->setPreventsSystemHTTPProxyAuthentication` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L64](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L64)
- [_WKWebsiteDataStoreConfiguration.mm#L711](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L711)
- [_WKWebsiteDataStoreConfiguration.mm#L716](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L716)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
