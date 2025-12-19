# ``WKInternalsNotes/WKWebsiteDataStore/_fetchDataRecordsOfTypes(_:withOptions:completionHandler:)``

指定したデータ種別のレコードを取得する。

## Objective-C Declaration
```objective-c
- (void)_fetchDataRecordsOfTypes:(NSSet<NSString *> *)dataTypes withOptions:(_WKWebsiteDataStoreFetchOptions)options completionHandler:(void (^)(NSArray<WKWebsiteDataRecord *> *))completionHandler;
```

## Discussion
`_WKWebsiteDataStoreFetchOption` から `WebsiteDataFetchOption` を構成し、`fetchData` の結果を `WKWebsiteDataRecord` 配列に変換する。

## References
- [`WKWebsiteDataStorePrivate.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L60)
- [`WKWebsiteDataStore.mm#L514`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L514)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
