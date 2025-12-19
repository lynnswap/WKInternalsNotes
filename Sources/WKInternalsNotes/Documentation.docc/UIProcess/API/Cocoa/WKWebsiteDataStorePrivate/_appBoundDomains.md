# ``WKInternalsNotes/WKWebsiteDataStore/_appBoundDomains(_:)``

App Bound Domains の一覧を返す。

## Objective-C Declaration
```objective-c
- (void)_appBoundDomains:(void (^)(NSArray<NSString *> *))completionHandler WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`ENABLE(APP_BOUND_DOMAINS)` 有効時は `getAppBoundDomains` の結果を文字列配列に変換して返す。無効時は空配列を返す。

## References
- [`WKWebsiteDataStorePrivate.h#L94`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L94)
- [`WKWebsiteDataStore.mm#L1170`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1170)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
