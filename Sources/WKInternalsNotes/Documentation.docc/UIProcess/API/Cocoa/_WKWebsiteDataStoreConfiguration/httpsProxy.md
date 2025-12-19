# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/httpsProxy``

HTTPS プロキシ設定を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy, setter=setHTTPSProxy:) NSURL *httpsProxy WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `httpsProxy` の値を返す。

## Discussion
getter は `_configuration->httpsProxy()` を `NSURL` に変換して返し、setter は `setHTTPSProxy` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L51](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L51)
- [_WKWebsiteDataStoreConfiguration.mm#L204](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L204)
- [_WKWebsiteDataStoreConfiguration.mm#L209](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L209)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
