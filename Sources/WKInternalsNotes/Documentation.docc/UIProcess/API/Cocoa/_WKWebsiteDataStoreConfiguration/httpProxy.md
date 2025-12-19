# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/httpProxy``

HTTP プロキシ設定を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy, setter=setHTTPProxy:) NSURL *httpProxy WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `httpProxy` の値を返す。

## Discussion
getter は `_configuration->httpProxy()` を `NSURL` に変換して返し、setter は `setHTTPProxy` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L50](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L50)
- [_WKWebsiteDataStoreConfiguration.mm#L194](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L194)
- [_WKWebsiteDataStoreConfiguration.mm#L199](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L199)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
