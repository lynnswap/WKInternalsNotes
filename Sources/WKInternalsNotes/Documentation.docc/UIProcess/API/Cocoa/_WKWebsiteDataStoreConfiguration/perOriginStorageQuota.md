# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/perOriginStorageQuota``

Origin ごとのストレージ容量上限を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) NSUInteger perOriginStorageQuota WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `perOriginStorageQuota` の値を返す。

## Discussion
getter は `_configuration->perOriginStorageQuota()` を返し、setter は `_configuration->setPerOriginStorageQuota` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L55](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L55)
- [_WKWebsiteDataStoreConfiguration.mm#L495](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L495)
- [_WKWebsiteDataStoreConfiguration.mm#L500](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L500)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
