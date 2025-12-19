# ``WKInternalsNotes/WKWebsiteDataStore/_getIsPrevalentDomain(_:completionHandler:)``

prevalent 判定の有無を取得する。

## Objective-C Declaration
```objective-c
- (void)_getIsPrevalentDomain:(NSURL *)domain completionHandler:(void (^)(BOOL))completionHandler WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
`isPrevalentResource` を呼び、結果を `completionHandler` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L84)
- [`WKWebsiteDataStore.mm#L1021`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1021)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
