# ``WKInternalsNotes/WKWebsiteDataStore/_scopeURL(_:hasPushSubscriptionForTesting:)``

テスト用に scope URL の Push 購読有無を確認する。

## Objective-C Declaration
```objective-c
-(void)_scopeURL:(NSURL *)scopeURL hasPushSubscriptionForTesting:(void(^)(BOOL))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`hasPushSubscriptionForTesting` を呼び、結果を `completionHandler` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L135)
- [`WKWebsiteDataStore.mm#L1440`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1440)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
