# ``WKInternalsNotes/WKWebsiteDataStore/_allowsCellularAccess``

セルラーアクセスの可否を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowsCellularAccess:) BOOL _allowsCellularAccess WK_API_DEPRECATED_WITH_REPLACEMENT("_WKWebsiteDataStoreConfiguration.allowsCellularAccess", macos(10.13.4, 10.15.4), ios(11.3, 13.4));
```

## Default Value
`YES`。

## Discussion
getter は `YES` を返し、setter は空実装。

## References
- [`WKWebsiteDataStorePrivate.h#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L67)
- [`WKWebsiteDataStore.mm#L898`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L898)
- [`WKWebsiteDataStore.mm#L902`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L902)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
