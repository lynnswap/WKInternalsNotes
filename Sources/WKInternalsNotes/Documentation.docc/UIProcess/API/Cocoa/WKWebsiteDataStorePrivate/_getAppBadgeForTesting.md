# ``WKInternalsNotes/WKWebsiteDataStore/_getAppBadgeForTesting(_:)``

テスト用にアプリバッジ値を取得する。

## Objective-C Declaration
```objective-c
-(void)_getAppBadgeForTesting:(void(^)(NSNumber *))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
`getAppBadgeForTesting` の結果があれば `NSNumber` にして渡し、無ければ `nil` を返す。

## References
- [`WKWebsiteDataStorePrivate.h#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L149)
- [`WKWebsiteDataStore.mm#L1502`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1502)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
