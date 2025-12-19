# ``WKInternalsNotes/WKWebsiteDataStore/_grantStorageAccessForTesting(_:withSubFrameDomains:completionHandler:)``

テスト用に Storage Access を付与する。

## Objective-C Declaration
```objective-c
- (void)_grantStorageAccessForTesting:(NSString *)topFrameDomain withSubFrameDomains:(NSArray<NSString *> *)subFrameDomains completionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
永続ストアでのみ `grantStorageAccessForTesting` を呼び、非永続では即 `completionHandler` を実行する。

## References
- [`WKWebsiteDataStorePrivate.h#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L79)
- [`WKWebsiteDataStore.mm#L950`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L950)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
