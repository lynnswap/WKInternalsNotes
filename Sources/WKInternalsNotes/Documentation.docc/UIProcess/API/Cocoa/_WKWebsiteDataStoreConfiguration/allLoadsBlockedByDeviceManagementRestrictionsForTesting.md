# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/allLoadsBlockedByDeviceManagementRestrictionsForTesting``

デバイス管理によるロードブロックをテスト用に強制する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL allLoadsBlockedByDeviceManagementRestrictionsForTesting WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持するフラグの初期値に従う。

## Discussion
getter は `_configuration->allLoadsBlockedByDeviceManagementRestrictionsForTesting()` を返し、setter は `_configuration->setAllLoadsBlockedByDeviceManagementRestrictionsForTesting` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L110](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L110)
- [_WKWebsiteDataStoreConfiguration.mm#L816](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L816)
- [_WKWebsiteDataStoreConfiguration.mm#L821](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L821)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
