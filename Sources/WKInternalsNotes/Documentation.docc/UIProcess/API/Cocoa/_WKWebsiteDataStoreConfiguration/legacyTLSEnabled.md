# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/legacyTLSEnabled``

レガシー TLS を有効にするかを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL legacyTLSEnabled WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `legacyTLSEnabled` の値を返す。

## Discussion
getter は `_configuration->legacyTLSEnabled()` を返し、setter は `_configuration->setLegacyTLSEnabled` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L61](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L61)
- [_WKWebsiteDataStoreConfiguration.mm#L686](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L686)
- [_WKWebsiteDataStoreConfiguration.mm#L691](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L691)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
