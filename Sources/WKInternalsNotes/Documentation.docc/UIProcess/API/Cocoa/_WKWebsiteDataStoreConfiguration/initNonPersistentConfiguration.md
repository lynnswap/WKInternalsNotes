# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/initNonPersistentConfiguration()``

非永続のデータストア構成を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initNonPersistentConfiguration WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
`API::Object::constructInWrapper<WebsiteDataStoreConfiguration>` を `IsPersistent::No` で呼び、非永続構成として初期化する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L41](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L41)
- [_WKWebsiteDataStoreConfiguration.mm#L52](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
