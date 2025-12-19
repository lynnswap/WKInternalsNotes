# ``WKInternalsNotes/WKWebsiteDataStore/_removeDataStoreWithIdentifier(_:completionHandler:)``

指定識別子のデータストアを削除する。

## Objective-C Declaration
```objective-c
+ (void)_removeDataStoreWithIdentifier:(NSUUID *)identifier completionHandler:(void(^)(NSError* error))completionHandler WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Discussion
識別子が `nil`/不正の場合は `NSError` を返し、正しい場合は `removeDataStoreWithIdentifier` のエラー文字列を `NSError` に変換して渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L56)
- [`WKWebsiteDataStore.mm#L776`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L776)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
