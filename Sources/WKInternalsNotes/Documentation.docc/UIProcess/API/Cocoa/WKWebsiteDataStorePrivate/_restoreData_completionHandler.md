# ``WKInternalsNotes/WKWebsiteDataStore/_restoreData(_:completionHandler:)``

バックアップデータを復元する。

## Objective-C Declaration
```objective-c
- (void)_restoreData:(NSData *)data completionHandler:(WK_SWIFT_UI_ACTOR void(^)(BOOL))completionHandler WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
`restoreData:completionHandler:` を呼び、エラー有無を `BOOL` に変換して返す。

## References
- [`WKWebsiteDataStorePrivate.h#L161`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L161)
- [`WKWebsiteDataStore.mm#L1599`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1599)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
