# ``WKInternalsNotes/WKWebsiteDataStore/_proxyConfiguration``

プロキシ設定を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setProxyConfiguration:) NSDictionary *_proxyConfiguration WK_API_DEPRECATED_WITH_REPLACEMENT("_WKWebsiteDataStoreConfiguration.proxyConfiguration", macos(10.14, 10.15.4), ios(12.0, 13.4));
```

## Default Value
`nil`。

## Discussion
getter は `nil` を返し、setter は空実装。

## References
- [`WKWebsiteDataStorePrivate.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L68)
- [`WKWebsiteDataStore.mm#L408`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L408)
- [`WKWebsiteDataStore.mm#L408`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L408)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
