# ``WKInternalsNotes/WKWebsiteDataStore/_appBoundSchemes(_:)``

App Bound Schemes の一覧を返す。

## Objective-C Declaration
```objective-c
- (void)_appBoundSchemes:(void (^)(NSArray<NSString *> *))completionHandler WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`ENABLE(APP_BOUND_DOMAINS)` 有効時は `getAppBoundSchemes` の結果を文字列配列に変換して返す。無効時は空配列を返す。

## References
- [`WKWebsiteDataStorePrivate.h#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L95)
- [`WKWebsiteDataStore.mm#L1184`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1184)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
