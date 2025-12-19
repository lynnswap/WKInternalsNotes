# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/allowsServerPreconnect``

サーバープリコネクトを許可するかを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL allowsServerPreconnect WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `allowsServerPreconnect` の値を返す。

## Discussion
getter は `_configuration->allowsServerPreconnect()` を返し、setter は `_configuration->setAllowsServerPreconnect` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L91](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L91)
- [_WKWebsiteDataStoreConfiguration.mm#L656](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L656)
- [_WKWebsiteDataStoreConfiguration.mm#L661](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L661)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
