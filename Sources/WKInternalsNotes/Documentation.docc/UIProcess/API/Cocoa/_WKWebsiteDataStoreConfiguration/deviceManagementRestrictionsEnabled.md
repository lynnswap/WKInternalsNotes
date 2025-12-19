# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/deviceManagementRestrictionsEnabled``

デバイス管理制限が有効かを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL deviceManagementRestrictionsEnabled WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `deviceManagementRestrictionsEnabled` の値を返す。

## Discussion
getter は `_configuration->deviceManagementRestrictionsEnabled()` を返し、setter は `_configuration->setDeviceManagementRestrictionsEnabled` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L52](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L52)
- [_WKWebsiteDataStoreConfiguration.mm#L465](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L465)
- [_WKWebsiteDataStoreConfiguration.mm#L470](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L470)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
