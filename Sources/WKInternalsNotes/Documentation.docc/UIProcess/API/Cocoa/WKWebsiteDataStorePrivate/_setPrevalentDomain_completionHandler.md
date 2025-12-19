# ``WKInternalsNotes/WKWebsiteDataStore/_setPrevalentDomain(_:completionHandler:)``

prevalent 判定を付与する。

## Objective-C Declaration
```objective-c
- (void)_setPrevalentDomain:(NSURL *)domain completionHandler:(void (^)(void))completionHandler WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
`setPrevalentResource` を呼び、完了後に `completionHandler` を実行する。

## References
- [`WKWebsiteDataStorePrivate.h#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L83)
- [`WKWebsiteDataStore.mm#L1014`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1014)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
