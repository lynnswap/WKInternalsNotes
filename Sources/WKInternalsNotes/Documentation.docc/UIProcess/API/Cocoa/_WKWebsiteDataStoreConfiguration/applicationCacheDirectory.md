# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/applicationCacheDirectory``

Application Cache の保存先ディレクトリを返す/設定する（deprecated）。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSURL *applicationCacheDirectory WK_API_DEPRECATED("ApplicationCache is no longer supported", macos(10.15.4, WK_MAC_TBA), ios(13.4, WK_IOS_TBA));
```

## Default Value
常に `nil` を返す。

## Discussion
getter は `nil` を返し、setter は空実装で何もしない。

## References
- [_WKWebsiteDataStoreConfiguration.h#L85](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L85)
- [_WKWebsiteDataStoreConfiguration.mm#L315](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L315)
- [_WKWebsiteDataStoreConfiguration.mm#L320](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L320)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
