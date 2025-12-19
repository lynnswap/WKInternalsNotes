# ``WKInternalsNotes/WKWebsiteDataStore/_isStorageSuspendedForTesting(_:)``

テスト用にストレージがサスペンド中か確認する。

## Objective-C Declaration
```objective-c
- (void)_isStorageSuspendedForTesting:(WK_SWIFT_UI_ACTOR void(^)(BOOL))completionHandler WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Discussion
`isStorageSuspendedForTesting` の結果を `completionHandler` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L163`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L163)
- [`WKWebsiteDataStore.mm#L1606`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1606)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
