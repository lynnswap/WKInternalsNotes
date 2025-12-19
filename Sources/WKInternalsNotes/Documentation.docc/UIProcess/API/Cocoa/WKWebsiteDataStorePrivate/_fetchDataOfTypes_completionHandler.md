# ``WKInternalsNotes/WKWebsiteDataStore/_fetchDataOfTypes(_:completionHandler:)``

指定したデータ種別のデータを取得する。

## Objective-C Declaration
```objective-c
- (void)_fetchDataOfTypes:(NSSet<NSString *> *)dataTypes completionHandler:(WK_SWIFT_UI_ACTOR void(^)(NSData *))completionHandler WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
`fetchDataOfTypes:completionHandler:` を呼び、エラーは無視して `NSData` を `completionHandler` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L160)
- [`WKWebsiteDataStore.mm#L1591`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1591)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
