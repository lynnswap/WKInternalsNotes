# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/proxyConfiguration``

プロキシ設定の辞書を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSDictionary *proxyConfiguration WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `proxyConfiguration` の値を返す。

## Discussion
getter は `_configuration->proxyConfiguration()` を `NSDictionary` にブリッジして返す。setter は引数を copy した上で `CFDictionaryRef` にブリッジし、`setProxyConfiguration` に渡す。

## References
- [_WKWebsiteDataStoreConfiguration.h#L62](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L62)
- [_WKWebsiteDataStoreConfiguration.mm#L696](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L696)
- [_WKWebsiteDataStoreConfiguration.mm#L761](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L761)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
