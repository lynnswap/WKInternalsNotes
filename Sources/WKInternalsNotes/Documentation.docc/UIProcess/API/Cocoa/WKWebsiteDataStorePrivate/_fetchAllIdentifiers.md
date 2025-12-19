# ``WKInternalsNotes/WKWebsiteDataStore/_fetchAllIdentifiers(_:)``

データストア識別子の一覧を取得する。

## Objective-C Declaration
```objective-c
+ (void)_fetchAllIdentifiers:(void(^)(NSArray<NSUUID *> *))completionHandler WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Discussion
`fetchAllDataStoreIdentifiers` で取得した ID を `NSUUID` 配列に変換して `completionHandler` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L55)
- [`WKWebsiteDataStore.mm#L764`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L764)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
