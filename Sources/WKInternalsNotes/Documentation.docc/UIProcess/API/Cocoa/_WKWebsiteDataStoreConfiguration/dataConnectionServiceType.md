# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/dataConnectionServiceType``

通信サービス種別を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSString *dataConnectionServiceType WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `dataConnectionServiceType` の値を返す。

## Discussion
getter は `_configuration->dataConnectionServiceType()` を `NSString` に変換して返し、setter は `_configuration->setDataConnectionServiceType` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L63](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L63)
- [_WKWebsiteDataStoreConfiguration.mm#L701](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L701)
- [_WKWebsiteDataStoreConfiguration.mm#L706](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L706)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
