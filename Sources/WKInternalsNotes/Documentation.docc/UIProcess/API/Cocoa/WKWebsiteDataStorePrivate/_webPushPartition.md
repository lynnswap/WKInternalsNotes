# ``WKInternalsNotes/WKWebsiteDataStore/_webPushPartition``

Web Push のパーティション文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *_webPushPartition;
```

## Default Value
初期値は configuration の `webPushPartitionString()` に依存する。

## Discussion
`configuration().webPushPartitionString()` を `NSString` に変換して返す。

## References
- [`WKWebsiteDataStorePrivate.h#L152`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L152)
- [`WKWebsiteDataStore.mm#L1482`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1482)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
