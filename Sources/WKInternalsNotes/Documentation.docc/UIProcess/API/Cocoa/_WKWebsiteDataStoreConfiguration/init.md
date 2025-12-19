# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/init()``

永続的なデータストア構成を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)init;
```

## Discussion
`API::Object::constructInWrapper<WebsiteDataStoreConfiguration>` を `IsPersistent::Yes` で呼び、永続構成として初期化する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L40](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L40)
- [_WKWebsiteDataStoreConfiguration.mm#L41](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
