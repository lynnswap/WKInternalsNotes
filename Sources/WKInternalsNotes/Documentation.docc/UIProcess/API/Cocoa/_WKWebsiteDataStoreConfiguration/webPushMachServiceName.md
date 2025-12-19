# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/webPushMachServiceName``

Web Push 用 Mach service 名を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy, setter=setWebPushMachServiceName:) NSString *webPushMachServiceName WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `webPushMachServiceName` の値を返す。

## Discussion
getter は `_configuration->webPushMachServiceName()` を `NSString` に変換して返し、setter は `_configuration->setWebPushMachServiceName` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L96](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L96)
- [_WKWebsiteDataStoreConfiguration.mm#L806](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L806)
- [_WKWebsiteDataStoreConfiguration.mm#L811](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L811)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
