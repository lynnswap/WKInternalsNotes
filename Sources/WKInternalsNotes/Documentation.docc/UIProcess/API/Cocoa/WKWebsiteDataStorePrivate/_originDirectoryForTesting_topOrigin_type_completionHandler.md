# ``WKInternalsNotes/WKWebsiteDataStore/_originDirectoryForTesting(_:topOrigin:type:completionHandler:)``

テスト用に origin のディレクトリパスを取得する。

## Objective-C Declaration
```objective-c
-(void)_originDirectoryForTesting:(NSURL *)origin topOrigin:(NSURL *)topOrigin type:(NSString *)dataType completionHandler:(void(^)(NSString *))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
データ型を `WebsiteDataType` に変換し、無効なら `nil` を返す。有効なら `originDirectoryForTesting` を呼び文字列で返す。

## References
- [`WKWebsiteDataStorePrivate.h#L136`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L136)
- [`WKWebsiteDataStore.mm#L1449`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1449)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
