# ``WKInternalsNotes/WKWebsiteDataStore/_getAllBackgroundFetchIdentifiers(_:)``

バックグラウンドフェッチ識別子の一覧を取得する。

## Objective-C Declaration
```objective-c
-(void)_getAllBackgroundFetchIdentifiers:(void(^)(NSArray<NSString *> *identifiers))completionHandler WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
`getAllBackgroundFetchIdentifiers` の結果を `NSString` 配列に変換して返す。

## References
- [`WKWebsiteDataStorePrivate.h#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L139)
- [`WKWebsiteDataStore.mm#L1369`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1369)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
