# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/pcmMachServiceName``

PCM 用 Mach service 名を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy, setter=setPCMMachServiceName:) NSString *pcmMachServiceName WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `pcmMachServiceName` の値を返す。

## Discussion
getter は `_configuration->pcmMachServiceName()` を `NSString` に変換して返し、setter は `_configuration->setPCMMachServiceName` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L95](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L95)
- [_WKWebsiteDataStoreConfiguration.mm#L796](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L796)
- [_WKWebsiteDataStoreConfiguration.mm#L801](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L801)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
