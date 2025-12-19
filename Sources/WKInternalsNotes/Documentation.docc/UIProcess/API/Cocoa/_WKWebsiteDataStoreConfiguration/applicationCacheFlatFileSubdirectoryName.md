# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/applicationCacheFlatFileSubdirectoryName``

Application Cache のサブディレクトリ名を返す/設定する（deprecated）。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSString *applicationCacheFlatFileSubdirectoryName WK_API_DEPRECATED("ApplicationCache is no longer supported", macos(10.4, WK_MAC_TBA), ios(13.4, WK_IOS_TBA));
```

## Default Value
常に `nil` を返す。

## Discussion
getter は `nil` を返し、setter は空実装で何もしない。

## References
- [_WKWebsiteDataStoreConfiguration.h#L86](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L86)
- [_WKWebsiteDataStoreConfiguration.mm#L324](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L324)
- [_WKWebsiteDataStoreConfiguration.mm#L329](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L329)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
