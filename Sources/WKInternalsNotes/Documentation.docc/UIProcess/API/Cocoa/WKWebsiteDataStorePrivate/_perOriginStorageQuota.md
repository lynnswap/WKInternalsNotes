# ``WKInternalsNotes/WKWebsiteDataStore/_perOriginStorageQuota``

Origin ごとのストレージ上限を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setPerOriginStorageQuota:) NSUInteger _perOriginStorageQuota WK_API_DEPRECATED_WITH_REPLACEMENT("_WKWebsiteDataStoreConfiguration.perOriginStorageQuota", macos(10.13.4, 10.15.4), ios(11.3, 13.4));
```

## Default Value
`0`。

## Discussion
getter は常に `0` を返し、setter は空実装。

## References
- [`WKWebsiteDataStorePrivate.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L64)
- [`WKWebsiteDataStore.mm#L880`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L880)
- [`WKWebsiteDataStore.mm#L880`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L880)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
